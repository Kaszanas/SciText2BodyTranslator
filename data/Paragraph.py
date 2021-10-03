from data.Sentence import Sentence


class Paragraph:
    def __init__(self):
        self.sentences = []

    def add_sentence(self, sentence: Sentence):
        self.sentences.append(sentence)

    def latex_get_paragraph(self):
        pass
