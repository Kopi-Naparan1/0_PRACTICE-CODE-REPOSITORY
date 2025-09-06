import re
import os

# Default folder to use
folder = os.path.join("C:/", "KOPI ANAN PASCO NAPARAN", "PROGRAMMING", "Python Course", "5 Advanced Python",
                      "Projects", "Project_Batch_1", "cache_files"
)


# Custom made file opener
class TemplateFile:
    def __init__(self, file , mode):
        self.file = file
        self.mode = mode
        self.handling = None

    def __enter__(self):
        print(f'Entered: {self.file}')
        self.handling = open(self.file, self.mode, encoding='utf-8')
        return self.handling

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.handling:
            self.handling.close()
            print(f'Exited: {self.file}')
            print()



def read_html(filename) -> str:
    file_name = os.path.join(folder, filename)

    with TemplateFile(file_name, 'r') as file:
        content = file.read()
        print('File loaded')
        return content


def write_html(filename, rendered):
    file_name = os.path.join(folder, filename)
    with TemplateFile(file_name, 'w') as file:
        file.write(rendered)
        print('File saved')


def replace_placeholder(match, context):
    """The idea is you will get anything that has this: {{x}}.
    After that, you will get the first part and/or the second position of that {{x | y}}"""
    parts: list[str] = match.group(1).split('|')
    key = parts[0].strip()  # gets the {{x}}
    default = parts[1].strip() if len(parts) > 1 else f"{{{{{key}}}}}"  # gets {{y}} if len > 1
    value = context.get(key, default)  # gets the value of the key, if not, tries default
    return escape_html(value)


def escape_html(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))


def main():
    context = {
        'name': "Nyro Kophalem",
        'email': "nyro@gmail.com"
    }

    content = read_html('project_1.5_template.html')

    rendered = re.sub(r'\{\{(.*?)\}\}', lambda m: replace_placeholder(m, context), content)

    write_html("test_template_1.5_rendered.html", rendered)


if __name__ =="__main__":
    main()