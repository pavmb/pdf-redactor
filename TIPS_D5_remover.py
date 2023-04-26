
import os
import re
import pdf_redactor

## Set options.
source_dir = "pdf/."
options = pdf_redactor.RedactorOptions()
options.content_filters = [
        (
                re.compile(r"d5([a-z]+)"),
                lambda m : "XXXXXXX"
        ),
        (
                re.compile(r"D5([A-Z]+)"),
                lambda m: "XXXXXXX"
        ),

]
# Perform the redaction using PDF on standard input and writing to standard output.

if __name__ == '__main__':
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".pdf"):
                filepath = os.path.join(root, file)
                options.input_stream = os.path.join(root, file)
                options.output_stream = os.path.join(root, file)
                try:
                    pdf_redactor.redactor(options)
                    print(f"{file} - Done")
                except:
                    print(f"{options.input_stream} - FAILED!!!!!!!!!")
