<!--Title-->
# File Processing
<!--Content Table-->
## Content


## Purpose
<!--Purpose of the project-->
This poject is a file processing program. The purpose of this project is to build a menu driven program using multiple function to edit a given input file and save the edited version in an output file. 

<!--Header 2 description of the project-->
## Description

<p style="text-align: justify">
The project is a menu driven program divided into multiple functions. The program starts by asking the for the input file that should contain a list of words one word in each line, the file should be a .txt file. Then the program will display the content of the file and create a list of all the words in the file using the **write_file** function. Then the program should display the menu and asks the user to choose whether to sort the list in ascending order using the **sort_list** function, sort the list in descending order using the **sort_list_desc** function, reverse the list using the **reverse_list** function, add a given word to the end of the list using the **add_word** function, add a line using the **add_line** function, remove a given word using the remove_word function and remove all occurences of a given word using the **remove_all_occurence** function. Each of these function uses the already built in function for lists in python such as sort, append, reverse, remove ... After the user chooses the option he wants he will be asked to provide the name of his output file. The edited list will be displayed along with the content of the output file. Finally the control will go back to repeat wich will keep on running the program as long as the user wants to edit a file and on each run he can edited a new file by providing its name.</p> 

<!--Header 3 installation and launching the project-->
## Getting Started

### Dependencies

<!--Link to install the latest version of g++-->
* You will need to have the latest version of g++ to run the program. g++ 8.1.0 (MinGW), a link is provided.
* [g++ 8.1.0 (MinGW)](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download)

### Installing
<!--Steps of Installation-->
* Download the g++ compiler and intall it. 
* Download the zip file and create a folder for it.

### Executing program
<!--Steps for running the program-->
#### How to run the program
* Look for Run Terminal in your search bar
* Open it and use the:
<!--commands to run the program "cd" change directory to where your files are-->
```
cd 
```
command to go to the specified directory.
* Use
<!--commands to run the program "make project" compile the program--> 
```
make project 
```
to compile the all the project files.
* Than type 
<!--commands to run the program "project" run and executes program-->
```
project 
```
to execute and run the program.

## Authors
<!-- The contributors to the project-->
* [Aicha Sidiya](https://github.com/AichaSidiya)
* Hanin Alzaher
* Thoraya Musa
* Rim Obaid


## Acknowledgments
<!-- Insparation files, codes, and general refrences used in writing the code of the project-->
* Book - C++ Programming. Program Design including Data Structures by D.S. Malik
* StatArray.h
* [Dynamic Array](https://www2.cs.sfu.ca/CourseCentral/225/johnwill/lab_arrays_intro.html)
* [C++ Pre-processor](https://doc.bccnsoft.com/docs/cppreference_en/preprocessor/all.html)
* [C++ documentation](https://www.cplusplus.com/doc/)
* [Readme Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Readme Content](https://ecotrust-canada.github.io/markdown-toc/)
