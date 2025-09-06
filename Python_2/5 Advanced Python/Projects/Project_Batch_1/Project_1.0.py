import re
import os

# Default folder to use
folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course", "5 Advanced Python",
                      "Projects", "Project_Batch_1", "cache_files"
)


# File opener/closer - custom alternative for open()
class TemplateFile:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.handle = None

    def __enter__(self):
        print(f'Entering the context of file: {self.file}')
        self.handle = open(self.file, self.mode, encoding='utf-8')

        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.handle:
            print(f'Exiting the context of file: {self.file}')
            self.handle.close()


def main():
    # Values are the replacement for the placeholder {{name}} or {{email}}
    context = {
        "name": "Nyro Kophalem",
        "email": "nryo@gmail.com"


    }

    filename_in: str = os.path.join(folder, 'template.html')

    # Opening/reading the file using the custom-made opener
    with TemplateFile(filename_in, 'r') as infile:
        content = infile.read()

    # Helper function - get the key's values. If not, return original key placeholder eg. {{name}}
    def replace_placeholder(match):
        key = match.group(1).strip()
        return context.get(key, f"{{{{{key}}}}}")

    rendered = re.sub(r'\{\{(.*?)\}\}', replace_placeholder, content)

    filename_out = os.path.join(folder, 'rendered.html')

    # Open/Write the text into html file
    with TemplateFile(filename_out, 'w') as outfile:
        outfile.write(rendered)

if __name__ == "__main__":
    main()