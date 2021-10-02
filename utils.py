import json
import logging
from string import Template
from typing import List

from Document import Document
from string_templates import LatexTemplates


def processing_pipeline(input_file, input_filepath: str, output_filepath: str):
    """
    processing_pipeline takes input file and calls specific parsing functions
    in order to generate the final output string
    that is going to be saved to drive
    """

    # Handling different input filetypes:
    if input_filepath.endswith(".json"):
        processed_json = parse_json(input_file=input_file)
    elif input_filepath.endswith(".md"):
        print("Currently not supported input filetype!")
        processed_json = parse_markdown()
    elif input_filepath.endswith(".tex"):
        print("Currently not supported input filetype!")
        processed_json = parse_latex()

    # Handling different output filetypes:
    if output_filepath.endswith(".tex"):
        # perform the function
        string_to_save = prepare_latex_string(input_object=processed_json)
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".md"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_md_string(input_object=processed_json)
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".json"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_json_string(input_object=processed_string)
        save_to_output(string_to_save, output_filepath)


def parse_json(input_file):

    """
    parse_json uses json.load() to parse the input file and returns Python object.
    """

    # Parse the JSON information and depending on the output filetype prepare the
    json_contents = json.load(input_file)

    document = Document()

    parsed_content_list = []
    for section_object in json_contents["content"]:

        if "sectionTitle" not in section_object:
            logging.error("sectionTitle key not found in the input json!")
            return [], False
        section_title = section_object["sectionTitle"]

        if "sectionLevel" not in section_object:
            logging.error("sectionLevel key not found in the input json!")
            return [], False
        section_level = section_object["sectionLevel"]

        if "paragraphBody" not in section_object:
            logging.error("paragraphBody not found in the input json!")
            return [], False

        section_body = []
        for sentence in section_object["paragraphBody"]:
            if "sentence" not in sentence:
                logging.error("paragraphBody object does not contain 'sentence' key!")
                return [], False
            if "citations" not in sentence:
                logging.error("paragraphBody object does not contain 'citations' key!")
                return [], False
            section_body.append(sentence)

        document.add_section(
            section_title=section_title,
            section_level=section_level,
            paragraph_body=section_body,
        )

    return document, True


def save_to_output(string_to_save: str, output_filepath: str):

    with open(output_filepath, "w") as output_file:
        output_file.write(string_to_save)


def parse_markdown():
    return ""


def parse_latex():
    return ""


def prepare_latex_string(document_class: Document) -> str:

    result_string = ""
    for section_title, section_level, paragraph_body, citation_list in document_class:
        template = Template(LatexTemplates.SECTION_TEMPLATE)

        formatted_string = ""
        if section_level == "1":
            citation_string = format_latex_citations(citation_list=citation_list)
            formatted_string = template.safe_substitute(
                section_title=section_title,
                paragraph_body=paragraph_body,
                citation_string=citation_string,
            )

            result_string += formatted_string

    return result_string


def format_latex_citations(citation_list: List) -> str:

    citation_string = ""
    for citation in citation_list:
        citation_string += f"{citation}, "

    citation_string = citation_string.rstrip(", ")

    return citation_string


def prepare_md_string(input_object) -> str:
    return ""


def prepare_json_string(input_object) -> str:
    return ""
