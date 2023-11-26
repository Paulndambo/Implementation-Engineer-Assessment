# Implementation-Engineer-Assessment - Paul Ndambo

# Prequisites
- Clone the folder containing all the files to your computer, use the following commands;-
    i. For https: ``git clone https://github.com/Paulndambo/Implementation-Engineer-Assessment.git``
    ii. for ssh: ``git clone git@github.com:Paulndambo/Implementation-Engineer-Assessment.git``
    iii. you can also download the zip file, clicking <link>https://github.com/Paulndambo/Implementation-Engineer-Assessment.git</link>
        and on the clone button options, select download as zip

- Make sure you clone the project, otherwise any of the stories below won't make sense unless you choose to view the project online, 
- Either way make sure you have access to the folder.

# Notes
- I have all answered all questions in Section A and selected Q2 in Section B
- Solutions, including runnable code examples will be found in the respective folders.
- For, example if you are looking for answers of Section A, Question 1, 
- Open the folder named Section A, inside it you will find a document and code examples 
- Will be found in a folder with the name of the Question.
- Also, please not that respective screenshots will be found inside folder with name
- corresponding to the question or section. 
- NB: Don't look for answers, code examples or screenshots of Section A in folder named SectionB, They are found in folder named SectionA

# NB
- After cloning/downloading the project, open your terminal/command prompt on the project, such that when you run ``ls``
- You see SectionA, SectionB, etc.


# Section A
- For this section, i have provided two things, that is;-
    i. A .docx file containing responses to the questions.
    ii. Two folders, each containing .py files, named according to the use of the file,
        and screenshots.

- To be able to run the .py files, you will need python installed and added to PATH on your computer
- Unlikely, but if you don't have python installed, you can install it as follows;-
    i. Go to python.org and click on the download button, or,
    ii. Inside anaconda on your computer, it will provide a python environment for you

- To run .py files, the command structure should be: python3 file_name.py,
- For example, ``python soap_example.py`` or ``python3 soap_example.py``

# Section B.
- For this section, you will find a django project which implements a simple search and results functionality.
- To run the django project locally;-
    i. Running Manually
        - Change directory to SectionB, that is, ``cd SectionB``
        - Create a virtual env, on mac and linux use ``python3 -m venv venv``
        - Activate virtual env, ``source venv/bin/activate``
        - Run the project as, ``python3 manage.py runserver``
    ii. Using Docker
        - To run the project using docker, 
        - change directory to SectionB, that is, ``cd SectionB``
        - run either of the commands below;-
            i. ``docker-compose up`` to run the project using docker compose
            ii. ``docker build -t sectionb . && docker run -p 8000:8000 --name backend sectionb`` to run as a docker container
