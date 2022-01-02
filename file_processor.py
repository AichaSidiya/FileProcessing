#the main function calls the other function and take inputs
print('***********************\tWelcome to your file processing program\t*********************')

def main():

    filename = input('\nPlease enter the name of your input file: ') + '.txt' #user input existing file with .txt

    print('\n******************\tPrinting the content of the input file\t**********************\n')
    read(filename) #calling the read function


    w_list = write_file(filename) #calling the write file fumction

    print('*****************\tThe List\t**********************\n\n', w_list) #printing the original list
    print('\n\n********************\tThe Menu\t******************\\n') #printing the menu

    #printing the option
    print('1 = Sort in ascending order \n2 = Sort in descending order' +
    '\n3 = Reverse \n4 = Add a word \n5 = Add a line \n6 = Remove a word '+
    '\n7 = Remove occurence of a word\n' )


    choice = int(input('What do you want to do?,Choose a number: ')) #inputing the choice of the user

    if choice == 1:

        outfile_name = input('\nPlease enter the name of your output file: ') + '.txt'

        sort_asc = sort_list(w_list) #calling the sort function

        print('\n********************\tThe list after ascending sorting\t*****************\n\n', sort_asc) #printing the updated list

        create_new_file(outfile_name, sort_asc)

    elif choice == 2:

        outfile_name = input('\nPlease enter the name of your output file: ') + '.txt'

        sort_dec = sort_list_desc(w_list) #calling the sort in descending order functions

        print('\n**************************\tThe list after descending sorting\t*********************\n\n', sort_dec) #printing the updated list

        create_new_file(outfile_name, sort_dec)

    elif choice == 3:

        outfile_name = input('\nPlease enter the name of your output file: ') + '.txt'

        reverse=reverse_list(w_list) #calling the reverse function

        print('\n*******************\tThe list after reversing\t**********************\n\n', reverse) #printing the updated list

        create_new_file(outfile_name, reverse)

    elif choice == 4:

        outfile_name=input('\nPlease enter the name of your output file: ') + '.txt'

        word1 = input('\nWhat word do you want to add: ') #asking the user about the word he wants to add

        add_w=add_word(w_list, word1) #calling the add word function

        print('\n**********************\tThe list after adding: ', word1, '\t*********************\n\n', add_w) #printing the updated list

        create_new_file(outfile_name, add_w)

    elif choice == 5:

        #taking input for the name of the new file
        new_file = input('\nPlease enter the name of your output file: ') + '.txt'

        add_line(w_list,new_file) #calling the add line function


    elif choice == 6:

        outfile_name = input('\nPlease enter the name of your output file: ') + '.txt'

        word2 = input('\nWhat word do you want to remove: ') #asking the user about the word he wants to remove

        remove = remove_word(w_list, word2) #calling the remove word funtion

        print('\n**********************\tThe new list after removing: ', word2, '\t**********************\n\n', remove) #printing the updated list

        create_new_file(outfile_name, remove)

    elif choice == 7:

        outfile_name = input('\nPlease enter the name of your output file: ') + '.txt'

        word3 = input('\nWhat word do you want to remove: ') #asking the user about the word he wants to remove

        remove_occurence = remove_all_occurence(w_list, word3) #calling the remove occurence funtion

        print('\n**********************\tThe new list after removing all occurences of: ', word3, '\t**************************\n\n', remove_occurence) #printing the updated list

        create_new_file(outfile_name, remove_occurence)

    else:
        print('\n******************\tWrong input!\t*******************\n') #if a we get a wrong input we print error


# reads the file who's name is given as an argument
def read(name):


    infile = open(name,'r') #openning the file in read mode.

    file_contents=infile.read()

    infile.close() #closing the file

    print(file_contents) #printing the content of the file

# this function writes the word in the file into a list
def write_file(name):

    create_list=[] #creating an empty list

    infile=open(name,'r') #openning file in read mode

    #loop that adds each word in the file to a list
    for word in infile:
        create_list.append(word.strip())
    return create_list

# this function sorts the list in ascending order
def sort_list(word_list):

    word_list.sort()
    return word_list

#this function sorts the list in descending order
def sort_list_desc(word_list):

    word_list.sort(reverse = True)
    return word_list

#this function reverse the list
def reverse_list(word_list):

    word_list.reverse()
    return word_list

#this function adds a word given as an argument to the end of the list
def add_word(word_list, word):

    word_list.append(word)
    return word_list

#this function creates a new file to put the list in and adds a line between each word of the list.
def add_line(word_list,name2):

    infile = open(name2, 'w') #openning the file in write mode

    #loop that adds each word of the list to the file while leaving a space in between
    for word in word_list:
        infile.write(word + '\n' + '\n')

    infile.close() #closing the file

    print('\n******************\tPrinting the content of the output file\t**********************\n')
    read(name2)

def remove_word(word_list, word_remove):


    #verifying if the word exist in the list
    try:
        word_list.remove(word_remove)

    except ValueError:

        print('\n********************\tThe word was not found in the list!\t********************\n')
        pass

    return word_list


# this function removes occurence of a word and leaves only on sample oof it.
def remove_all_occurence(word_list, word):

    #verifying if the word exist in the list
    try:
        counts = word_list.count(word)

        while counts>1:
            word_list.remove(word)
            counts-=1

    except ValueError:

        print('\n********************\tThe word was not found in the list!\t********************\n')
        pass

    return word_list


#creatimg an output file
def create_new_file(name3, word_list):

    outfile=open(name3, 'w') #openning in write mode

    for word in word_list:
        outfile.write(word + '\n')

    #closing the file
    outfile.close()

    print('\n******************\tPrinting the content of the output file\t**********************\n')
    read(name3)


#this function call the main and repeat it as long as answer=yes
def repeat():

    print('\nDo you want to edit a file? ')
    answer = input('y or Y: ')

    while answer == 'y' or answer == 'Y':

        main()

        print('\nDo you want to edit another file? ')
        answer = input('y or Y: ')

    if answer != 'y' or answer != 'Y':

        print('\n*********************\tThank you, bye\t**************************\n')

repeat()
