import argparse
import os
import json

from utils import process_json, save_to_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to translate the body of text in formats such as json<->markdown<->latex"
    )
    parser.add_argument(
        "--input_file", default="./input.json", help="Specifies input file in the supported format."
    )
    parser.add_argument(
        "--output_file",
        default="./output.tex"
        help="Specifies the output file that will be created in supported format.",
    )

    args = parser.parse_args()

    input_filepath = args.input_file
    with os.open(input_filepath, "r") as input_file:
        if input_filepath.endswith(".json"):
            processed_string = process_json(input_file)
            save_to_output(processed_string, args.output_file)
        elif input_filepath.endswith(".md"):
            print("Currently not supported input filetype!")
        elif input_filepath.endswith(".tex"):
            print("Currently not supported input filetype!")
