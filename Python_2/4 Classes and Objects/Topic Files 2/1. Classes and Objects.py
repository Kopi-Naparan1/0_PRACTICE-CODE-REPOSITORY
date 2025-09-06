
class Book:
    def info(self, title, author, year):
        print(f'Title: {title} - Author: {author} - Year: {year} ')


book_1 = Book()  # book_1 is the object. "Book" is the class
book_1.info("The Best", "Kopi", 2000)
