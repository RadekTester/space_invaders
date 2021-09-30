# space_invaders

### Intro
This is a Python 3.x application. It has been developed and tested with Python 3.8.

### Files and Folders structure: 

- *main.py* --- can be used to run the application 
- *config.py* --- file containing configuration of the application
- *.gitignore* --- file which specifies for git, which of the files should be ignored
- *README.md* --- This file. Serves as documentation for the application
- *.flake8* --- File with flake8 (PEP8) ignore statements
- *requirements.txt* --- File containing list of required python packages.
- */tests* --- folder containing tests and test data
- */src* --- folder containing source code of the application
- */venv* --- folder containing Python virtual environment 


### Installation of virutal environment
In order for the appliaction to work, please ensure that you have created your Python virtual environment
`python -m venv venv`

Activate your virtual environment (on Windows machine): 
`.\venv\Scripts\activate`

Then ensure that you upgrade your pip. 
`python -m pip install --upgrade pip`

Then ensure that you have installed all necessary packages with: 
`pip install -r requirements.txt`


### Details of the application
- Goal of the application is to identify intruders on radar scan
- Radar scan is distorted with noise
- It is considered, that not always a 'perfect' intruder picture will be visible. Therefore Probability function has been developed to calculate probability of seeing a intruder


### Coordinates
Coordinates are provides with x and y. 
x is horizontal from left to right
y is vertical from top to bottom

x=0, y=0
+----------
|  x-> 
|  y 
|  |
|  

### Assumptions
- Intruder and Radar scans will be perfect rectangulars. If not, application will raise exception about that.