<!--Title-->
# File Processing
<!--Content Table-->
## Content
- [File Processing](#file-processing)
  * [Content](#content)
  * [Purpose](#purpose)
  * [Description](#description)
  * [How to run the program](#how-to-run-the-program)
  * [Authors](#authors)
  * [Acknowledgments](#acknowledgments)

## Purpose
<!--Purpose of the project-->
This poject is a file processing program. The purpose of this project is to build a menu driven program using multiple function to edit a given input file and save the edited version in an output file.

<img src="https://github.com/AichaSidiya/FileProcessing/blob/main/demoFiles.gif"/>

<!--Header 2 description of the project-->
## Description

<p style="text-align: justify">
The project is a menu driven program divided into multiple functions. The program starts by asking the for the input file that should contain a list of words one word in each line, the file should be a .txt file. Then the program will display the content of the file and create a list of all the words in the file using the <b>write_file</b> function. Then the program should display the menu and asks the user to choose whether to sort the list in ascending order using the <b>sort_list</b> function, sort the list in descending order using the <b>sort_list_desc</b> function, reverse the list using the <b>reverse_list</b> function, add a given word to the end of the list using the <b>add_word</b> function, add a line using the <b>add_line</b> function, remove a given word using the remove_word function and remove all occurences of a given word using the <b>remove_all_occurence</b> function. Each of these function uses the already built in function for lists in python such as sort, append, reverse, remove ... After the user chooses the option he wants he will be asked to provide the name of his output file. The edited list will be displayed along with the content of the output file. Finally the control will go back to repeat wich will keep on running the program as long as the user wants to edit a file and on each run he can edited a new file by providing its name.</p>

## Menu
* (1) Sort Ascending
* (2) Sort Descending
* (3) Reverse
* (4) Add word
* (5) Add line
* (6) Remove word
* (7) Remove occurences

<!--Header 3 installation and launching the project-->
## How to run the program
* Clone the repository to your local machine:
```
git clone https://github.com/AichaSidiya/FileProcessing.git
``` 
* Install [Python3](https://www.python.org/downloads/)
* Verify python is insalled by typing
```
python
```   
in your command prompt
* Execute the program using: 

```
python file_processor.py
```

## Authors
<!-- The contributors to the project-->
* [Aicha Sidiya](https://github.com/AichaSidiya)
* [Hanin Alzaher](https://github.com/hanin-az)
* Thoraya Musa
* Rim Obaid


## Acknowledgments
<!-- Insparation files, codes, and general refrences used in writing the code of the project-->
* Book - Starting Out with Python FOURTH EDITION by Tony Gaddis
* [Remove All Occurences](https://www.geeksforgeeks.org/remove-all-occurrences-of-a-character-in-a-string/)
* [Readme Template](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)
* [Readme Content](https://ecotrust-canada.github.io/markdown-toc/)
