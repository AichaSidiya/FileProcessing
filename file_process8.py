#the main function calls the other function and take inputs
def main():
    #verifying the inputs
    try:
    #user input existing file with .txt
        filename=input('filename input file:')

    except IOError:
        print('the file name you entered does not exist please enter an existing file')

    #calling the read function
    read(filename)
    #calling the write file fumction
    w_list=write_file(filename)
    #printing the original list
    print('The list: ',w_list)
    #printing the option
    print('1= sort in ascending order \n2=sort in descending order' +
    '\n3= reverse \n4= add a word \n 5= add a line \n6= remove a word '+
    '\n 7= remove occurence of a word' )
    #inputing the choice of the user
    choice=int(input('what do you want to do?,choose the number'))
    if choice==1:
        outfile_name=input('filename output file:')
        #calling the sort function
        sort_asc=sort_list(w_list)
        #printing the updated list
        print('The list after ascending sorting: ',sort_asc)
        create_new_file(outfile_name, sort_asc)
    elif choice==2:
        outfile_name=input('filename output file:')
        #calling the sort in descending order function
        sort_dec=sort_list_desc(w_list)
        #printing the updated list
        print('The list after descending sorting: ',sort_dec)
        create_new_file(outfile_name, sort_dec)
    elif choice==3:
        outfile_name=input('filename output file:')
        #calling the reverse function
        reverse=reverse_list(w_list)
        #printing the updated list
        print('The list after reversing: ',reverse)
        create_new_file(outfile_name, reverse)
    elif choice==4:
        outfile_name=input('filename output file:')
        #asking the user about the word he wants to add
        w=input('What word do you want to add:')
        #calling the add word function
        add_w=add_word(w_list, w)
        #printing the updated list
        print(w_list)
        create_new_file(outfile_name, add_w)
    elif choice==5:
        #taking input for the name of the new file
        new_file=input('filename:')
        #calling the add line function
        add_line(w_list,new_file)
    elif choice==6:
        outfile_name=input('filename output file:')
        #calling the remove word funtion
        remove=remove_word(w_list)
        #printing the updated list
        print('The new list:',remove)
        create_new_file(outfile_name, remove)
    elif choice==7:
        outfile_name=input('filename output file:')
        #asking the user about the word he wants to remove
        w2=input('What word do you want to remove:')
        #calling the remove occurence funtion
        occurence=remove_occurence(w_list, w2)
        #printing the updated list
        print('the new list:',occurence)
        create_new_file(outfile_name, occurence)
    else:
        print('error') #if a we get a wrong input we print error


# reads the file who's name is given as an argument
def read(name):
    #openning the file in read mode.
    infile=open(name,'r')
    file_contents=infile.read()
    #closing the file
    infile.close()
    #printing the content of the file
    print('File contents:',file_contents)

# this function writes the word in the file into a list
def write_file(name):
    #creating an empty list
    create_list=[]
    infile=open(name,'r') #openning file in read mode
    #loop that adds each word in the file to a list
    for word in infile:
        create_list.append(word.strip())
    return create_list

# this function sorts the list in ascending order
def sort_list(word_list):
    word_list.sort()
    return word_list

#this function orts the list in descending order
def sort_list_desc(word_list):
    word_list.sort(reverse=True)
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
    #openning the file
    infile=open(name2, 'w')
    #loop that adds each word of the list to the file while leaving a space in between
    for word in word_list:
        infile.write(word + '\n' + '\n')
    #closing the file
    infile.close()

def remove_word(word_list):
    #verifying if the word exist in the list
    word=input('What word do you want to remove:')
    try:
        word_list.remove(word)
    except ValueError:
        print('the word was not found in the list')
        word=input('What word do you want to remove:')
        word_list.remove(word)

    return word_list
# this function removes occurence of a word and leaves only on sample oof it.
def remove_occurence(word_list, word):
    counts=word_list.count(word)
    while counts>1:
        word_list.remove(word)
        counts-=1
    return word_list
#creatimg an output file
def create_new_file(name3, word_list):
    outfile=open(name3, 'w') #openning in write mode
    for word in word_list:
        outfile.write(word + '\n')
    #closing the file
    outfile.close()


#this function call the main and repeat it as long as answer=yes
def repeat():
    print('do you want to edit a file?')
    answer=input('y or Y:')
    while answer=='y' or answer=='Y':
        main()
        print('do you want to edit another file?')
        answer=input('y or Y:')
    if answer!='y' or answer!='Y':
        print('Thank you, bye')

repeat()
