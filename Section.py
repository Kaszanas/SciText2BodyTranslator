from string_templates import LatexTemplates
from string import Template

from Sentence import Sentence

from typing import List


class Section:
    def __init__(
        self, section_title: str, section_level: int, section_body: List[Sentence]
    ):

        self.section_title = section_title
        self.section_level = section_level
        self.section_body = section_body

        self.formatted_sentences = ""

    def latex_format_section(self) -> str:

        """latex_format_section formats a whole LaTeX section and returns a string.

        Returns:
            str: LaTeX section string with citations.
        """

        # Checking the section level to select proper section template:
        if self.section_level == "1":
            section_template = Template(LatexTemplates.SECTION_TEMPLATE_1)
        elif self.section_level == "2":
            section_template = Template(LatexTemplates.SECTION_TEMPLATE_2)
        elif self.section_level == "3":
            section_template = Template(LatexTemplates.SECTION_TEMPLATE_3)

        # Formatting sentences that can have interlocked citations:
        self.__latex_format_sentences()

        # Creating the final section string
        section_string = section_template.safe_substitute(
            section_title=self.section_title,
            formatted_section_body=self.formatted_sentences,
        )

        return section_string

    def __latex_format_sentences(self):

        for sentence in self.section_body:
            self.formatted_sentences += sentence.latex_get_sentence()
