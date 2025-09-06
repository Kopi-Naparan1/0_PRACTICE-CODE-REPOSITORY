
def assignment3():
    class Book:
        number_of_pages = 300

        def __init__(self, title, author):
            self.title = title
            self.author = author

        def display(self):
            print(f'Title: {self.title} \n'
                  f'Author: {self.author}\n'
                  f'Pages: {self.number_of_pages}')
            print('')

    book1 = Book('Lino King', "Eric")
    book2 = Book("Love", 'Lovely')
    book1.display()
    book2.display()









def main():
    print('STARTING THE #2\n')

    assignment3()





if __name__ == "__main__":
    main()