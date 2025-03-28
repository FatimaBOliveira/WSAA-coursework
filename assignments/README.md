# Web Services and Applications - Assignments

This subdirectory contains my approach to the assignments for the module Web Services and Applications in the Higher Diploma in Science in Computing in Data Analytics course, [ATU Galway Mayo](https://www.gmit.ie/).

This README follows the instructions from [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) on how to write README files.

## About this project

This subdirectory includes:

- 3 python files:
    - [assignment2-carddraw.py](), it's a program that reads an API that deals a deck of cards, tells the user the value and suit of his hand of cards and checks if there's any good combination;
    - [assignment03-cso.py](), reads a RESTFul API from CSO regarding the Exchequer Account (Historical Series), and saves the data in a json file;
    - [assignment04-github.py](), reads a file from a repository, modifies this file and commits into my GitHub account;
- and a [json folder](), with the json files generated by the assignments 3 and 4.

Each python file corresponds to one assignment, all containing a brief explanation of the programs, the steps taken to do them, and the references that helped me to complete them. The Python code used follows the [PEP 8](https://realpython.com/python-pep8/) coding style as standard.

## Purpose of this project

The purpose of this work is interact with API's and other files found online, developing competencies in how to interact with this type of data.

## How to run this project

To run the programs, [Anaconda](https://www.anaconda.com/download) and [Visual Studio Code](https://code.visualstudio.com/Download) need to be installed to run Python code and visualize the data on any machine. After that, this subdirectory can be [cloned in VSC](https://github.com/MicrosoftDocs/azure-dev-docs/blob/main/articles/javascript/how-to/with-visual-studio-code/clone-github-repository.md) as instructed by Microsoft.

## Dependencies

The [requirements.txt](https://github.com/FatimaBOliveira/Programming-for-data-analytics/blob/main/requirements.txt) file, found in the root of this repository, indicates all the packages needed in order to run these programs. This file was generated through the command line with the code `pip freeze > requirements.txt`, as instructed by [Microsoft Docs](https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/python/managing-required-packages-with-requirements-txt.md). To download the packages on any machine, use the code `pip install -r requirements.txt`.

## Usage

The users need the programs listed above, and ensure that all dependencies are installed. To successfully run the programs, in both assignment 3 and 4, both need a slight change:
- In assignment 3, in function `getAsFile()`, in `"./json/cso.json"`, make sure you have a json folder in your current directory, otherwise just write `"./cso.json"` instead in order to generate the new file;
- In assignment 4, users need their own config.py file with the keys that they can get in their onw GitHub account. This config.py file should never be committed to GitHub as others can use these keys and make changes in our account. Then users need to change the name of the repository in `repo = g.get_repo("FatimaBOliveira/WSAA-coursework")` with their onw, and then finally change the path where the file will be stored.

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token

## Get help

If there's any problem with this project, please submit [issues](https://github.com/FatimaBOliveira/Programming-for-data-analytics/issues) in this repository.

## Author

**by Fatima Oliveira** 

Email: g00438857@atu.ie or Fatima.21.00@hotmail.com