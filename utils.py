import json
from string import Template
from string_templates import SECTION_TEMPLATE

from typing import List


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
        string_to_save = prepare_latex_string(
            input_object=processed_json, template_string=SECTION_TEMPLATE
        )
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

    parsed_content_list = []
    for section_object in json_contents:

        section_level = 0
        if "sectionLevel" in paragraph_object:
            section_level = paragraph_object["sectionLevel"]

        section_title = ""
        if "sectionTitle" in paragraph_object:
            section_title = paragraph_object["sectionTitle"]

        paragraph_body = ""
        if "paragraphBody" in paragraph_object:
            paragraph_body = paragraph_object["paragraphBody"]

        citations = []
        if "citations" in paragraph_object:
            citations = paragraph_object["citations"]

        parsed_content_list.append(
            (section_title, section_level, paragraph_body, citations)
        )

    return parsed_content_list


def save_to_output(string_to_save: str, output_filepath: str):

    with open(output_filepath, "w") as output_file:
        output_file.write(string_to_save)


def parse_markdown():
    return ""


def parse_latex():
    return ""


def prepare_latex_string(input_object, template_string: str) -> str:

    template = Template(template_string)

    result_string = ""
    for section_title, section_level, paragraph_body, citation_list in input_object:

        if section_level == 1:
            citation_string = format_latex_citations(citation_list=citation_list)
            template.substitute(
                section_title=section_title,
                paragraph_body=paragraph_body,
                citation_string=citation_string,
            )

    return template.__str__()


def format_latex_citations(citation_list: List) -> str:

    citation_string = ""
    for citation in citation_list:
        citation_string += f"{citation}, "

    return citation_string


def prepare_md_string(input_object) -> str:
    return ""


def prepare_json_string(input_object) -> str:
    return ""
