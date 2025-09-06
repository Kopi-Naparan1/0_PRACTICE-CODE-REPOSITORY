from abc import ABC, abstractmethod


class FormField(ABC):
    def __init__(self, label, name, required=True, placeholder=''):
        self.label = label
        self.name = name
        self.required = required
        self.placeholder = placeholder

    @abstractmethod
    def render(self):
        pass

    def render_label(self):
        return f'<label for="{self.name}"> {self.label}</label>'

    def __str__(self):
        return self.render()


class TextField(FormField):
    def render(self):
        req = " required" if self.required else ''

        return (f'\t{self.render_label()}\n'
                f'\t<input type="text" name="{self.name}" placeholder="{self.placeholder}" {req}>')


class EmailField(FormField):
    def render(self):
        req = " required" if self.required else ''

        return (f'\t{self.render_label()}\n'
                f'\t<input type="email" name="{self.name}" placeholder="{self.placeholder}" {req}>')


class PasswordField(FormField):
    def render(self):
        req = " required" if self.required else ''

        return (f'\t{self.render_label()}\n'
                f'\t<input type="password" name="{self.name}" placeholder="{self.placeholder}" {req}>')


def main():
    fields = [
        TextField("Username", "username", required=True, placeholder="Enter your Username: "),
        EmailField("Email", "email", required=True, placeholder="Enter your Email: "),
        PasswordField("Password", "password", required=True, placeholder="Enter your Password: "),
    ]
    print('<form>')
    print('\t<h2>User Registration</h2>\n')
    for field in fields:
        print(f"{field}")
        print()
    print('\t<button type="submit">Submit</button>')
    print('</form>')
if __name__ == "__main__":
    main()