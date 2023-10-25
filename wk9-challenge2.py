'''
2.	Extending Library Item Class
Library and Book Classes: Extend the Library Item class in (1)
with a Book class with data attributes for a book’s title, author, publisher
and an additional attributes as number of pages,
and a Boolean data attribute indicating whether there is both hard copy and eBook version of the book.
Demonstrate Book Class in a Tester Program with an object of Book class.
'''

import Library_and_Book_Class
from Library_and_Book_Class import Library
from Library_and_Book_Class import Book


def main():
    # Local variables
    item_name = ''
    author = ''
    publisher = 0
    pages = ''
    version = False

    # Get data attributes.
    item_name = input('Enter the item name: ')
    author = input('Enter the author: ')
    publisher = input('Enter the publisher: ')
    pages = input('Enter the pages: ')
    version = input('Whether it has both hard copy and eBook version? (Yes/No) ')

    if version == 'Yes':
        version = True
    else:
        version = False

    # Create an instance of Customer.
    book_1 = Book(item_name, author, publisher, pages, version)

    # Display Customer Information.
    print('Book information: ')
    print('Book Name:', book_1.get_item_name())
    print('Author:', book_1.get_author())
    print('Publisher:', book_1.get_publisher())
    print('Number of its page:', book_1.get_pages())
    print('Whether it has both hard copy and eBook version:', book_1.get_version())


# Call the main function.
main()
