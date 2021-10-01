import argparse
import os
import json

from utils import processing_pipeline

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
    output_filepath = args.output_file
    with os.open(input_filepath, "r") as input_file:
        processing_pipeline(input_file=input_file, input_filepath=input_filepath, output_filepath=output_filepath)
