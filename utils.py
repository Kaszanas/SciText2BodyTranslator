import json

def process_json(input_file):
    json_contents = json.load(input_file)

    initialized_string = ""
    for section in json_contents["content"]:
        # Parse the JSON information and depending on the output filetype prepare the 


def save_to_output(string_to_save, output_filepath):

    if output_filepath.endswith(".tex"):
        # perform the function
    elif output_filepath.endswith(".md"):
        print("Output filetype not supported yet!")
    elif output_filepath.endswith(".json"):
        print("Output filetype not supported yet!")

def prepare_latex_string():
    pass

def prepare_md_string():
    pass

def prepare_json_string():
    pass