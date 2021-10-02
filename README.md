# SciText2BodyTranslator

SciText2BodyTranslator is a tool that is built to ease the scientific manuscript creation process.
Currently available tools such as pandoc (markdown, LaTeX) with filters do not provide enough easy workflows for scientific work that is fit to be sent to scientific publishers.

## Proposed workflow

0. Prepare Your content in a JSON or Markdown format.
1. Find the LaTeX template that is provided by the publisher.
2. Perform the translation from JSON either to markdown or to LaTeX
3. Fill out the body of the LaTeX template that You have obtained before
4. Compile Your paper.

## JSON Schema

```
{"content" : [
    {"sectionName": string, "sectionLevel": int, "paragraphBody": [{"sentence": string, "citations": [string]}]},
    {"sectionName": string, "sectionLevel": int, "paragraphBody": [{"sentence": string, "citations": [string]}]}
    ...
    ]
}
```

## License

This program is licensed under GNU GPL v3 if You wish to obtain a different license, please contact the author directly.