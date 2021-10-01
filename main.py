import argparse
import os
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Tool to translate the body of text in formats such as json<->markdown<->latex"
    )
    parser.add_argument(
        "--input_file", help="Please provide input file in the supported format."
    )
    parser.add_argument(
        "--output_file",
        help="Please provide the output file that will be created in supported format.",
    )
