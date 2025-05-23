# Web Services and Applications - Project

This subdirectory contains my project for the module Web Services and Applications in the Higher Diploma in Science in Computing in Data Analytics course, [ATU Galway Mayo](https://www.gmit.ie/).

This README follows the instructions from [Github](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) on how to write README files.

## About this project

This project demonstrates how to build a web application using [Flask](https://flask.palletsprojects.com/en/stable/quickstart/) with a [RESTful API](https://aws.amazon.com/what-is/restful-api/) that connects to a [MySQL](https://dev.mysql.com/doc/refman/8.4/en/what-is-mysql.html) database. The application performs [CRUD](https://www.freecodecamp.org/news/crud-operations-explained/#heading-what-is-crud) (Create, Read, Update, Delete) and other operations through [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) pages.

This subdirectory includes:

- [server.py](https://github.com/FatimaBOliveira/WSAA-coursework/blob/main/project/server.py): The main file of this project that, when called, runs a Flask server, allowing users to view and manipulate database data in real time through HTML pages;
- [PatientDAO.py](https://github.com/FatimaBOliveira/WSAA-coursework/blob/main/project/PatientDAO.py) and [TreatmentDAO.py](https://github.com/FatimaBOliveira/WSAA-coursework/blob/main/project/TreatmentDAO.py): These [DAOs](https://en.wikipedia.org/wiki/Data_access_object) (Data Access Objects) are responsible for executing database operations in MySQL, such as loading, inserting, updating, and deleting data related to treatments and patients;
- [interface](https://github.com/FatimaBOliveira/WSAA-coursework/tree/main/project/interface) folder: Includes HTML pages for displaying and interacting with the data. Each page is composed of `<head>` and `<body>` sections for customizing the layout, along with a `<script>` section that contains JavaScript functions for handling forms, interactions, data validation, and [AJAX](https://api.jquery.com/jQuery.ajax/) calls to the Flask server to perform CRUD operations. The treatment HTML page also includes additional operations, such as fetching treatments for a specific patient.
- [mysql](https://github.com/FatimaBOliveira/WSAA-coursework/tree/main/project/mysql) folder: Contains Python files that allow the creation of the database and tables, and the manipulation of data in MySQL.

This project uses a hidden [configuration file](https://martin-thoma.com/configuration-files-in-python/), dbconfig.py, that is used in the DAOs and in the Python files in mysql folder. The purpose of this file is to store sensitive information with MySQL database credentials.

I hosted my project in [PythonAnywhere](https://www.pythonanywhere.com/about/company_details/), and the page can be found here: https://fatimaboliveira.pythonanywhere.com/. To host, I created an account, and cloned this repository. Then, in the HTML pages, I changed the ports of the AJAX calls. I also needed to set up a MySQL database in PythonAnywhere.

The Python code used follows the [PEP 8](https://realpython.com/python-pep8/) coding style as standard.

The main resources for this project are based on code from Professor Andrew Beatty, web searches, and ChatGPT.

## Purpose of this project

The main objectives of this work are:
- Learn how to create a Flask web server with a RESTful API, which allows the user to perform CRUD and other operations in the database;
- develop  skills in creating HTML pages, that display and manipulate the data with javaScripts and Ajax calls;
- Learn how to connect the back-end Python files with the front-end HTML to interact with the database;
- Learn how to host the project on an external platform, PythonAnywhere.

This project was very useful for me as it provided a practical example of integrating front-end and back-end using a RESTful API, resulting in a fully functional web application for managing data.

## Getting Started

To use this project, [Anaconda](https://www.anaconda.com/download) and [Visual Studio Code](https://code.visualstudio.com/Download) (VSC) need to be installed. After that, this subdirectory can be [cloned in VSC](https://github.com/MicrosoftDocs/azure-dev-docs/blob/main/articles/javascript/how-to/with-visual-studio-code/clone-github-repository.md) as instructed by Microsoft. 

Another essential program is MySQ, as this is where the database of this project is located. To download it, please follow the official instructions provided on the [MySQL website](https://dev.mysql.com/doc/refman/8.4/en/installing.html).

Also a Web browser is needed to open and interact with the online application. After this, the project should run easily.

## Dependencies

The [requirements.txt](https://github.com/FatimaBOliveira/Programming-for-data-analytics/blob/main/requirements.txt) file, found in the root of this repository, indicates all the packages needed in order to run the Python code. This file was generated through the command line with the code `pip freeze > requirements.txt`, as instructed by [Microsoft Docs](https://github.com/MicrosoftDocs/visualstudio-docs/blob/main/docs/python/managing-required-packages-with-requirements-txt.md). To run this project on any machine, clone this repository and download the packages through the terminal of VSC with `pip install -r requirements.txt`.

## Usage

The project runs when server.py is executed, then it can be accessed through web browser at the [localhost](https://dev.to/richardshaju/what-is-localhost-in-development-mode-2ecn) port 5000, http://127.0.0.1:5000. All the [endpoints](https://blog.postman.com/what-is-an-api-endpoint/) are defined in the server.py, and most of them return a JSON-formatted data, while the last two use the HTML pages incorporated. 

All the files in this subdirectory are crucial elements for the users to deploy this project, as these are inter-connected. Additionally, before running the project, please create your own configuration file with your MySQL credentials. Also, the database and the tables must be created first before trying to do CRUD operations. These can be set manually in MySQL or through running the python files that are found in mysql folder.

Also, users need the programs listed above, and ensure that all dependencies are installed. 

To avoid any other issues, please ensure that no other application is using localhost port 5000, that MySQL is running on your machine, and all files are in the correct directory structure as they are organized here.

## Get help

If there's any problem with this project, please submit [issues](https://github.com/FatimaBOliveira/Programming-for-data-analytics/issues) in this repository.

## Author

**by Fatima Oliveira** 

Email: g00438857@atu.ie or Fatima.21.00@hotmail.com