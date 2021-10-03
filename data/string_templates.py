class LatexTemplates:

    SECTION_TEMPLATE_1 = """\section{$section_title}\n\n$formatted_section_body\n\n"""

    SECTION_TEMPLATE_2 = (
        """\subsection{$section_title}\n\n$formatted_section_body\n\n"""
    )

    SECTION_TEMPLATE_3 = (
        """\subsubsection{$section_title}\n\n$formatted_section_body\n\n"""
    )

    PARAGRAPH_TEMPLATE = """$paragraph \n"""

    SENTENCE_TEMPLATE_CITATIONS = """$sentence \cite{$citation_string} """

    SENTENCE_TEMPLATE_NO_CITATIONS = """$sentence """
