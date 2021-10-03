from typing import List
from string import Template

from data.string_templates import LatexTemplates


class Sentence:
    def __init__(self, sentence_text: str, citation_list: List):
        self.sentence_text = sentence_text
        self.citation_list = citation_list

        self.formatted_sentence = ""
        self.citation_string = ""

    def latex_get_sentence(self):

        """latex_get_sentence is returning a string of single sentence with or without citations."""

        self.__latex_format_sentence()

        return self.formatted_sentence

    def __latex_format_sentence(self):

        # Initially setting the sentence template not to contain citations because there might be certain sentences without citations:
        sentence_template = Template(LatexTemplates.SENTENCE_TEMPLATE_NO_CITATIONS)

        # If citations should be created formatting sentence with citations and go to next iteration
        if not self.citation_list == []:
            citation_string = self.__latex_format_citations()
            sentence_template = Template(LatexTemplates.SENTENCE_TEMPLATE_CITATIONS)

            formatted_string = sentence_template.safe_substitute(
                sentence=self.sentence_text, citation_string=citation_string
            )

            self.formatted_sentence = formatted_string
        else:
            # Sentence without citation is created if there are no citaions present in citation list:
            formatted_string = sentence_template.safe_substitute(
                sentence=self.sentence_text
            )

            self.formatted_sentence = formatted_string

    def __latex_format_citations(self) -> str:

        """__latex_format_citations takes a section list and creates a string that is a properly formatted LaTeX citation.

        Returns:
            str: Returns a string of LaTeX citations.
        """

        if not self.citation_list == []:
            for citation in self.citation_list:
                self.citation_string += f"{citation}, "

            self.citation_string = self.citation_string.rstrip(", ")

        return self.citation_string
