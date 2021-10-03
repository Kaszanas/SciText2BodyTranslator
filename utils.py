import json
import logging
from string import Template
from typing import List

from Document import Document
from Sentence import Sentence
from string_templates import LatexTemplates


def processing_pipeline(input_file, input_filepath: str, output_filepath: str):
    """
    processing_pipeline takes input file and calls specific parsing functions
    in order to generate the final output string
    that is going to be saved to drive
    """

    # Handling different input filetypes:
    if input_filepath.endswith(".json"):
        document_class, parsingOk = parse_json(input_file=input_file)
        if not parsingOk:
            return
    elif input_filepath.endswith(".md"):
        print("Currently not supported input filetype!")
        processed_json, parsingOk = parse_markdown()
        if not parsingOk:
            return
    elif input_filepath.endswith(".tex"):
        print("Currently not supported input filetype!")
        processed_json, parsingOk = parse_latex()
        if not parsingOk:
            return

    # Handling different output filetypes:
    if output_filepath.endswith(".tex"):
        # perform the function:
        string_to_save = document_class.latex_string()
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".md"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_md_string(input_object=processed_json)
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".json"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_json_string(input_object=processed_string)
        save_to_output(string_to_save, output_filepath)


def latex_pipeline():
    pass


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
            return Document(), False
        section_title = section_object["sectionTitle"]

        if "sectionLevel" not in section_object:
            logging.error("sectionLevel key not found in the input json!")
            return Document(), False
        section_level = section_object["sectionLevel"]

        if "sectionBody" not in section_object:
            logging.error("sectionBody not found in the input json!")
            return Document(), False

        section_body = []
        for sentence in section_object["sectionBody"]:
            if "sentenceText" not in sentence:
                logging.error("sectionBody object does not contain 'sentenceText' key!")
                return Document(), False
            if "citations" not in sentence:
                logging.error("sectionBody object does not contain 'citations' key!")
                return Document(), False
            section_body.append(
                Sentence(
                    sentence_text=sentence["sentenceText"],
                    citation_list=sentence["citations"],
                )
            )

        document.add_section(
            section_title=section_title,
            section_level=section_level,
            section_body=section_body,
        )

    return document, True


def save_to_output(string_to_save: str, output_filepath: str):

    with open(output_filepath, "w") as output_file:
        output_file.write(string_to_save)


def parse_markdown():
    return Document(), False


def parse_latex():
    return Document(), False
