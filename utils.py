import json


def processing_pipeline(input_file, input_filepath: str, output_filepath: str):
    """
    processing_pipeline takes input file and calls specific parsing functions
    in order to generate the final output string
    that is going to be saved to drive
    """
    pass

    if input_filepath.endswith(".json"):
        processed_string = parse_json(input_file, output_filepath)

    elif input_filepath.endswith(".md"):
        print("Currently not supported input filetype!")
        processed_string = parse_markdown()
    elif input_filepath.endswith(".tex"):
        print("Currently not supported input filetype!")
        processed_string = parse_latex()

    if output_filepath.endswith(".tex"):
        # perform the function
        string_to_save = prepare_latex_string()
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".md"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_md_string()
        save_to_output(string_to_save, output_filepath)
    elif output_filepath.endswith(".json"):
        print("Output filetype not supported yet!")
        string_to_save = prepare_json_string()
        save_to_output(string_to_save, output_filepath)


def parse_json(input_file):

    """
    parse_json uses json.load() to parse the input file and returns Python object.
    """

    # Parse the JSON information and depending on the output filetype prepare the
    json_contents = json.load(input_file)
    return json_contents


def save_to_output(string_to_save: str, output_filepath: str):
    pass


def parse_markdown():
    return ""


def parse_latex():
    return ""


def prepare_latex_string(input_string: str) -> str:
    return ""


def prepare_md_string(input_string: str) -> str:
    return ""


def prepare_json_string(input_string: str) -> str:
    return ""
