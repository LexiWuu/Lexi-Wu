'''
Challenge Activity 1: Library Information System GUI
Design a GUI for Book view class for the following Library Information System,
which you have worked on in Week 9 Challenge Activity 1
'''

import Library_and_Book_Class
from Library_and_Book_Class import Library
from Library_and_Book_Class import Book
import tkinter as tk

class LibraryGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Book Information Display System")

        # set the container frames
        self.item_name_frame = tk.Frame(self.main_window)
        self.author_frame = tk.Frame(self.main_window)
        self.publisher_frame = tk.Frame(self.main_window)
        self.pages_frame = tk.Frame(self.main_window)
        self.version_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)
        self.info_frame = tk.Frame(self.main_window)

        # get Book data
        # create and pack the widgets for Book's name
        self.item_name_label = tk.Label(self.item_name_frame, text='Enter the item name: ')
        self.item_name_entry = tk.Entry(self.item_name_frame, width=20)
        self.item_name_label.pack(side='left')
        self.item_name_entry.pack(side='left')

        # create and pack the widgets for book's author
        self.author_label = tk.Label(self.author_frame, text='Enter the author: ')
        self.author_entry = tk.Entry(self.author_frame, width=20)
        self.author_label.pack(side='left')
        self.author_entry.pack(side='left')

        # create and pack the widgets for book's publisher
        self.publisher_label = tk.Label(self.publisher_frame, text='Enter the publisher: ')
        self.publisher_entry = tk.Entry(self.publisher_frame, width=20)
        self.publisher_label.pack(side='left')
        self.publisher_entry.pack(side='left')

        # create and pack the widgets for book's pages
        self.pages_label = tk.Label(self.pages_frame, text='Enter the pages: ')
        self.pages_entry = tk.Entry(self.pages_frame, width=20)
        self.pages_label.pack(side='left')
        self.pages_entry.pack(side='left')

        # create and pack the widgets for book's version choice
        self.version_label = tk.Label(self.version_frame,
                                      text='Whether it has both hard copy and eBook version? (Yes/No) ')
        self.version_label.pack(side='left')
        # create and pack the widgets for version buttons
        # the Radio buttons
        self.radio_var = tk.IntVar()
        # set the intVar object to 1.
        self.radio_var.set(1)
        self.rb1 = tk.Radiobutton(self.version_frame, text='Yes', variable=self.radio_var, value=1)
        self.rb2 = tk.Radiobutton(self.version_frame, text='No', variable=self.radio_var, value=0)
        # pack the Radio buttons
        self.rb1.pack()
        self.rb2.pack()

        # create a display button and a quit button
        self.display_button = tk.Button(self.button_frame, text='Display', command=self.display_person_info)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        # pack the buttons
        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')

        # create info display multiline text area
        self.info_text_area = tk.Text(self.info_frame, bg='light blue', height=20, width=40)
        self.info_text_area.pack()

        # pack the frames
        self.item_name_frame.pack()
        self.author_frame.pack()
        self.publisher_frame.pack()
        self.pages_frame.pack()
        self.version_frame.pack()
        self.button_frame.pack()
        self.info_frame.pack()
        # wait in the main loop until event handler click
        tk.mainloop()

    # event handler call back function (display book info button)
    def display_person_info(self):
        # get the person details from GUI and store them in variables
        item_name = (self.item_name_entry.get())
        author = (self.author_entry.get())
        publisher = (self.publisher_entry.get())
        pages = (self.pages_entry.get())
        version = (self.radio_var.get())
        # create an instance of Library/Book
        book_1 = Book(item_name, author, publisher, pages, version)

        # display the data that was entered
        self.info_text_area.delete("1.0", "end")
        disp_string = ""
        version = ""
        disp_string += 'Here is the Book Information: '
        disp_string += "\n-------------------------------"
        disp_string += '\nItem name: ' + book_1.get_item_name()
        disp_string += '\nAuthor: ' + book_1.get_author()
        disp_string += '\nPublisher number: ' + book_1.get_publisher()
        disp_string += '\nPages: ' + book_1.get_pages()
        if book_1.get_version() == 1:
            version = 'Yes'
        else:
            version = 'No'
        disp_string += '\nWhether it has both hard copy and eBook version: ' + version

        self.info_text_area.insert("1.0", disp_string)

        # end of display_person_info() event handler /call back method


LibraryGUI()
