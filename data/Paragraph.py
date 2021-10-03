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

        self.__latex_format_sentences()

        output_string = paragraph_template.safe_substitute(
            paragraph=self.formatted_sentences
        ).rstrip(" ")

        return output_string

    def __latex_format_sentences(self):

        pos = -1
        for sentence in self.sentences:
            pos += 1
            if pos == len(self.sentences) - 1:
                self.formatted_sentences += sentence.latex_get_sentence().rstrip()
                continue

            self.formatted_sentences += sentence.latex_get_sentence()
