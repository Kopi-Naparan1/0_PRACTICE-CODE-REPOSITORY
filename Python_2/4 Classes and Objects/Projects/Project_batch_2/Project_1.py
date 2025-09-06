import random
from string import ascii_letters, digits


class URLShortener:

    def __init__(self):
        self.character_pool = list(ascii_letters + digits)
        self.code_to_url = {}
        self.url_to_code = {}

    def generate_code(self):
        return ''.join(random.choices(self.character_pool,6))

    def add_url(self, long_url):
        if long_url in self.url_to_code:
            code = self.url_to_code[long_url]
            print(f'Url: {long_url} is already inside the data base: ')
            return code
        else:
            code = self.generate_code()  # Ensures that code is unique
            while code in self.code_to_url:
                code = self.generate_code()

            self.code_to_url[code] = long_url
            self.url_to_code[long_url] = code
            print(f'[+] Your URL code {code}')
            return code

    def get_url(self, code):
        if code in self.code_to_url:
            long_url = self.code_to_url[code]
            print(f"[+] Your URL: {long_url}")
            return long_url
        else:
            print(f'URL with code: {code} is not found')
            return None


def main():

    shortener = URLShortener()
    code_1 = shortener.add_url("www.google.com")
    url_1 = shortener.get_url(code_1)





if __name__ == "__main__":
    main()