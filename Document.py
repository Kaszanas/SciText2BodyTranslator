from Section import Section
from Sentence import Sentence
from typing import List


class Document:
    def __init__(self):
        self.section_list = []

    def add_section(
        self, section_title: str, section_level: int, section_body: List[Sentence]
    ):
        """Adds a section to document

        Args:
            section_title (str): Title of the section.
            section_level (int): level of the section that defines if the section is a subsection or just a section.
            section_body (List[Sentence]): List of sentences that build up the seciton text.
        """

        self.section_list.append(
            Section(
                section_title=section_title,
                section_level=section_level,
                section_body=section_body,
            )
        )

    def latex_string(self):
        result_string = ""

        for section in self.section_list:
            result_string += section.latex_format_section()

        return result_string
