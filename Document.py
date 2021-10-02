class Document:
    def __init__(self):
        self.section_list = []

    def add_section(self, section_title, section_level, paragraph_body):
        """Adds a section to document

        Args:
            section_title (str): [description]
            section_level (int): [description]
            paragraph_body (List): [description]
        """

        self.section_list.append(section_title, section_level, paragraph_body)

    def prepare_latex_string():
        result_string = ""

        for (
            section_title,
            section_level,
            paragraph_body,
            citation_list,
        ) in self.section_list:
            template = Template(LatexTemplates.SECTION_TEMPLATE)

            formatted_string = ""
            if section_level == "1":
                citation_string = format_latex_citations(citation_list=citation_list)
                formatted_string = template.safe_substitute(
                    section_title=section_title,
                    paragraph_body=paragraph_body,
                    citation_string=citation_string,
                )

                result_string += formatted_string

        return result_string
