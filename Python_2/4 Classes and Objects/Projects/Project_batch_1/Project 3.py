class Library:
    total_books = 150

    def borrow_books(self, amount = 0):
        if amount <= 0:
            print("Didn't borrow any books.")

        elif 5 >= amount <= Library.total_books:
            Library.total_books -= amount
            print(f'Borrow {amount} books')

        else:
            print('Invalid number of books to borrow.')

    def return_books(self, amount = 0):
        if amount <= 0:
            print("Didn't return any books.")
        elif 5 >= amount and amount + Library.total_books <= 150:
            Library.total_books += amount
            print(f'Return {amount} books.')
        else:
            print('Invalid number of books to return.')

    def check_remaining_books(self):
        print(f'Remaining Books: {Library.total_books}')


person_1 = Library()
person_1.check_remaining_books()
person_1.return_books(0)

person_1.borrow_books(5)

person_1.check_remaining_books()

person_1.return_books(5)

person_1.check_remaining_books()
person_1.return_books(1)