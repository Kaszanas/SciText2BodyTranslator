from data.Section import Section
from data.Sentence import Sentence
from typing import List


class Document:
    def __init__(self):
        self.section_list = []

    def add_section(self, section: Section):
        """Adds a section to document"""

        self.section_list.append(section)

    def latex_string(self):
        result_string = ""

        for section in self.section_list:
            result_string += section.latex_format_section()

        return result_string

    def markdown_string(self):
        return ""

    def json_string(self):
        return ""
