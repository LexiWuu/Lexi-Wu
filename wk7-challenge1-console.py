# get the file name as input from the user
file_name = str(input('Enter the name of the file: '))
print(f'{file_name} has been successfully created.')


def words_write():
    print('========Words Report========')
    # get the number of words the user will input
    number_words = int(input('Enter how many words would you like to write to a file: '))
    # open output file
    output_file = open(file_name, 'w')
    # get each word and write it to the file
    for counter in range(number_words):
        word = str(input('Enter the words, one at a time: '))
        output_file.write(word + '\n')

    # close the file
    output_file.close()
    print("The words for the file are saved.")


def words_read():
    print("========Reading Words Report========")
    length = 0
    total = 0
    counter = 0
    # open input file
    input_file = open(file_name, 'r')
    # split the file into several words
    words = input_file.read().split()
    # go through all the words
    for i in words:
        length = len(i)  # get the length of each word
        counter += 1  # keep calculating the number of words
        total += length  # calculate the total length of all the words
    # get the longest word
    longest = max(words, key=len)
    print('The longest word in the file is: ', longest)
    print('The number of words in the file is: ', counter)
    avg_len = total / counter
    print('The average length of all the words in the file is: ', avg_len)
    # close the file
    input_file.close()


def main():
    words_write()
    words_read()


try:
    main()
except IOError:
    print('An error occurred while trying to read the file.')
except ValueError:
    print('None data found in the file')
except:
    print('An error occurred')
