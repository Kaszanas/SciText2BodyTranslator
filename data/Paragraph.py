from data.Sentence import Sentence
from data.string_templates import LatexTemplates

from string import Template


class Paragraph:
    def __init__(self):
        self.sentences = []
        self.formatted_sentences = ""

    def add_sentence(self, sentence: Sentence):
        self.sentences.append(sentence)

    def latex_get_paragraph(self):
        paragraph_template = Template(template=LatexTemplates.PARAGRAPH_TEMPLATE)

        output_string = paragraph_template.safe_substitute(
            paragraph=self.formatted_sentences
        )

        return output_string

    def __latex_format_sentences(self):

        for sentence in self.sentences:
            self.formatted_sentences += sentence.latex_get_sentence()
