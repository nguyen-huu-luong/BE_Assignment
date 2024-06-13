# BACK-END ASSIGNMENT
Hi all, this is my repository for this assignment
## Source Code Structure
There are three main folders: input, output, src <br/>
- input: This folder contains three provided mock files: pdf_mock_file.pdf, docx_mock_file.docx, Networking.pptx
- output: This folder contains output files after executing code
- src: This folder contains code for four questions. In specific,
    - question1.py: Implement script for question 1
    - question2and3.py: Implement sciprt for question 2 and question 3
    - question4.py: Implement sciprt for question 4
    - helper.py: Implement shared functions and import all necessary packages
- requirements.txt: This file contains imported packages
- docker-compose.yml, Dockerfile, startup.sh: These files are used to run code by Docker

## Executing code
There are two ways to run this code
- Run with Docker
    - After pulling code, go the source code folder and run this command
        ```
        docker-compose up
        ```
- Run manually
    - After pulling code, go the source code folder and install necessary packages
        ```
        pip install -r requirements.txt
        ```
        Go to src folder
        ```
        cd ./src
        ```
    - Run script of question 1
        ```
        python question1.py 
        ```
    - Run script of question 2 and question 3
        ```
        python question2and3.py
        ```
    - Run script of question 4
        ```
        python question4.py 
        ```
