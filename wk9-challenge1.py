'''
1.	Library Item Class Design and Testing
Design a class that holds the Library Item Information, with item name, author, publisher.
Write appropriate accessor and mutator methods.
Also, write a tester program that creates three instances/objects of the Library Items class.
'''

import Library_and_Book_Class
from Library_and_Book_Class import Library


def main():
    # Create three instances/objects of Person Class
    book1_info = Library('The Great Gatsby', 'F. Scott Fitzgerald', "Charles Scribner's Sons")
    book2_info = Library('Cien años de soledad', 'Gabriel García Márquez', "Editorial Sudamericana")
    book3_info = Library('Pride and Prejudice', 'Jane Austen', "T. Egerton")

    print('Information of The Great Gatsby:')
    display_info(book1_info)
    print()
    print("Information of Cien años de soledad:")
    display_info(book2_info)
    print()
    print("Information of Pride and Prejudice:")
    display_info(book3_info)


def display_info(info):
    print('Item name: ', info.get_item_name())
    print('Author: ', info.get_author())
    print('Publisher: ', info.get_publisher())


# Call the main function.
main()
