import json
import logging
from string import Template
from typing import List

from data.Document import Document
from data.Section import Section
from data.Paragraph import Paragraph
from data.Sentence import Sentence
from data.string_templates import LatexTemplates


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
        document_class, parsingOk = parse_markdown()
        if not parsingOk:
            return
    elif input_filepath.endswith(".tex"):
        print("Currently not supported input filetype!")
        document_class, parsingOk = parse_latex()
        if not parsingOk:
            return

    # Handling different output filetypes:
    if output_filepath.endswith(".tex"):
        # perform the function:
        string_to_save = document_class.latex_string()
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".md"):
        print("Output filetype not supported yet!")
        string_to_save = document_class.markdown_string()
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".json"):
        print("Output filetype not supported yet!")
        string_to_save = document_class.json_string()
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

        section = Section(section_title=section_title, section_level=section_level)

        for paragraph_object in section_object["sectionBody"]:

            paragraph = Paragraph()

            for sentence_object in paragraph_object["paragraph"]:
                if "sentenceText" not in sentence_object:
                    logging.error(
                        "sentence_object does not contain 'sentenceText' key!"
                    )
                    return Document(), False
                if "citations" not in sentence_object:
                    logging.error(
                        "sentence_object object does not contain 'citations' key!"
                    )
                    return Document(), False
                paragraph.add_sentence(
                    sentence=Sentence(
                        sentence_text=sentence_object["sentenceText"],
                        citation_list=sentence_object["citations"],
                    )
                )
            section.add_paragraph(paragraph=paragraph)

        document.add_section(section)

    return document, True


def save_to_output(string_to_save: str, output_filepath: str):

    with open(output_filepath, "w") as output_file:
        output_file.write(string_to_save)


def parse_markdown():
    return Document(), False


def parse_latex():
    return Document(), False
