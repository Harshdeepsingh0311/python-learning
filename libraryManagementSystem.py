# Library Management System

class Library:

    def __init__(self, list, name):
        self.books_list = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f'We have following books in the library: {self.name}')
        for book in self.books_list:
            print(book)

    def lend_books(self, person, book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:person})
            print('Lender Book database has been updated')

        else:
            print(f'Book is already being used by {self.lend_dict[book]}')

    def add_book(self, book):
        self.books_list.append(book)
        print('Book has been added!!')

    def return_book(self, book):
        self.lend_dict.pop(book)

if __name__ == '__main__':
    harshdeep = Library(['Python', 'C++', 'Java', 'CSS'], 'Code with me')

    while True:
        try:
            print(f'Welcome to the {harshdeep.name} library. Enter your choice to continue:  ')
            print('1, Display Book')
            print('2, Lend Book')
            print('3, Add Book')
            print('4, Return Book')
            user_choice = int(input())

            if user_choice == 1:
                harshdeep.display_books()

            elif user_choice == 2:
                book = input('Enter name of the book you want to lend: ')
                user = input('Enter your name: ')
                harshdeep.lend_books(user, book)

            elif user_choice == 3:
                book = input('Enter name of the book you want to add: ')
                harshdeep.add_book(book)

            elif user_choice == 4:
                book = input('Enter name of the book you want to return: ')
                harshdeep.return_book(book)

            else:
                print('Not a valid option')

            user_choice2 = ''
            while user_choice2 != 'c' and user_choice2 != 'q':
                user_choice2 = input('Press q to quit and c to continue ')
                if user_choice2 == 'q':
                    pass
                if user_choice2 == 'c':
                    continue

        except Exception as e:
            print(e)