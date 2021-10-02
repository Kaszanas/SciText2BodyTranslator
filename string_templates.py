class LatexTemplates:

    SECTION_TEMPLATE = """\section{$section_title}\n\n$paragraph_body\n\n"""

    SUBSECTION_TEMPLATE = """\subsection{$section_title}\n\n$paragraph_body\n\n"""

    SENTENCE_TEMPLATE = """$sentence \cite{$citation_string}"""
