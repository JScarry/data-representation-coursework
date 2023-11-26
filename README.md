# data-representation-coursework

## This repository contains data-representation-coursework

### Author: Jarlath Scarry

### Repository contains 

                Assignments folder
                Labs folder
                .gitignore
                Readme
                requirements.txt
                

# Instructions: 

## Instructions to run Labs:
Labs are mostly python files (These can be identified a .py extension). To run these you will need capability to run python on your machine. You should also download the full folder contents as there are some dependant files lab folders. After downloading the lab                  folder run the .py file. 
For example, to run trains_lab.py, you should download the lab01_trains folder and run the trains_lab.py from the folder.

A list of Python packages required to run all labs and assignments is included in the requirements.txt file. When you have setup python and a virtual environment to run the files the required extra packages can be installed by rinning the command `pip install -r requirements.txt`


## Instructions to run Assignments:

Most assignments can be run with the same steps as used fro running labs (see above). Specific instructions for each assignment are          listed below.
A list of Python packages required to run all labs and assignments is included in the requirements.txt file. When you have setup python and a virtual environment to run the files the required extra packages can be installed by rinning the command `pip install -r requirements.txt`
  
  
### Instructions to run Assignment1.1
                XML file that store data for a library (Library created manually)
                The library has two catalogues (technical books, and cookery books).
                    Each catalogue can contain a number of books. 
                            Books have an ISBN, title and author.
                Run the Library.py to search the XML library file
                

### Instructions to run Assignment03

Python program that retrieves the dataset for the "exchequer account (historical series)". Gets data from UPL: "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/WHAT--WE--SPECIFY/JSON-stat/2.0/en"
Stores data into a file called "cso.json".


### Instructions to run Assignment04
Python file. 
Run the python program to access my Github. The program is set to access a private repository "JScarry/aPrivateRepository"
                
You will not be able to access this private repository without the config.py file.It holds the API key

The program:
Accesses the a file called text.txt in the private repository.
It reads the contents as a string, searches for the word Andrew and replaces it with Jarlath.
Then updates the file on Github by pushing the modified file to Github by a commit.
Update comment seen on Github is "updated by prog"



### End



