import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog


class WordsReportGUI:
    def __init__(self):

        # create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Words Report")

        # create two frames to group widgets
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # create the widgets for the top frame
        self.words_label = tkinter.Label(self.top_frame,
                                         text='Enter how many words would you like to write to a file: ')
        self.words_entry = tkinter.Entry(self.top_frame, width=10)

        # pack the top frame's widgets
        self.words_label.pack(side='left')
        self.words_entry.pack(side='left')

        # create the button widgets for the bottom frame
        self.words_write_button = tkinter.Button(self.bottom_frame,
                                                 text='Words Report',
                                                 command=self.words_write)
        self.words_read_button = tkinter.Button(self.bottom_frame,
                                                text='Reading Words Report',
                                                command=self.words_read)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # pack the buttons
        self.words_write_button.pack()
        self.words_read_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

    # the words_write and words_read methods are callback functions for two Calculate buttons
    def words_write(self):
        # get the number of words the user will input
        num_words = int(self.words_entry.get())
        # open output file
        output_file = open('words_report', 'w')
        messagebox.showinfo("showinfo", "'Enter the words, one at a time: '")
        # get each word and write it to the file
        for count in range(1, num_words + 1):
            words_done = str(simpledialog.askstring(title="The No." + str(count) + "word: )",
                                                    prompt="Enter Your word: "))
            output_file.write(str(words_done) + '\n')

        # close the file
        output_file.close()
        messagebox.showinfo("showinfo", "The words report created.\n Now click on Display Words Report button.")

    def words_read(self):
        disp_string = ""
        try:
            # open input file
            input_file = open('words_report', 'r')
            disp_string += "Here is my words report: \n"
            length = 0
            total = 0
            counter = 0
            # split the file into several words
            words = input_file.read().split()
            # go through all the words
            for i in words:
                length = len(i)  # get the length of each word
                counter += 1  # keep calculating the number of words
                total += length  # calculate the total length of all the words
            # get the longest word
            longest = max(words, key=len)
            disp_string += '\nThe longest word in the file is: ' + str(longest) + '.\n'
            disp_string += '\nThe number of words in the file is: ' + str(counter) + '.\n'
            avg_len = total / counter
            disp_string += '\nThe average length of all the words in the file is: ' + str(avg_len) + '.\n'
            # close the file
            input_file.close()
            # print(disp_string)
            messagebox.showinfo("showinfo", disp_string)

        except IOError:
            messagebox.showinfo("Error", "Could not open file")
        except ValueError:
            print('None data found in the file')
        except:
            print('An error occurred')


my_sales_tracker = WordsReportGUI()
