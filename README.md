# space_invaders

### Intro
This is a Python 3.x application. It has been developed and tested with Python 3.8.
It is not using any fancy features so it should work with lower version of Python 3.x as well

### Files and Folders structure: 

- *main.py* --- can be used to run the application 
- *config.py* --- file containing configuration of the application
- *.gitignore* --- file which specifies for git, which of the files should be ignored
- *README.md* --- This file. Serves as documentation for the application
- *.flake8* --- File with flake8 (PEP8) ignore statements
- *requirements.txt* --- File containing list of required python packages.
- */tests* --- folder containing tests and test data
- */src* --- folder containing source code of the application
- */venv* --- folder containing Python virtual environment (it will be created automatically after running installation)
- */scan_data* --- folder containing provided sample data in for of text files.


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
- Goal of the application is to identify intruders on a radar scan.
- Radar scan is distorted with noise.
- It is considered, that not always a 'perfect' intruder picture will be visible. Therefore min matching "pixels" are required to indicate intruder.
- Appliaction returns intruders locations (top left correner x, y location), as well as % of matching pixels and visibility on scan %.


### Coordinates
Coordinates are provides with x and y. 
x is horizontal from left to right
y is vertical from top to bottom

x=0, y=0 is the top left corner
+----------
|  x-> 
|  y 
|  |
|  

### Assumptions
- Intruder and Radar scans will be perfect rectangulars.
- Intrudes do not rotate. There is no rotation of the intruder logic implemented. It could be added in the future.
- If 85% (parameter in config.py) of the "pixels" match intruder, we are considering this a match and positively identified intruder.
- Intruders might be entering the radar range. Therefore at the edges we might have intrudres, but not yet fully visible.
--- Logic is implemented in a way that it starts detecting intruders before they are visible as a whole. E.g., half of the intruder might be visible at the edge.
--- In intruder is not visible on the screen matching pixels percentage is increased proportianlly (more than 85% match is required). This is to eliminate false positives.


### Results for sample data provided
location: 16, 28 | intruders visibility: 100 %| matching pixels: 55| matching pixels %: 86%

location: 42, 0 | intruders visibility: 100 %| matching pixels: 56| matching pixels %: 88%

location: 60, 13 | intruders visibility: 100 %| matching pixels: 80| matching pixels %: 91%

location: 74, 1 | intruders visibility: 100 %| matching pixels: 77| matching pixels %: 88%

location: 82, 41 | intruders visibility: 100 %| matching pixels: 55| matching pixels %: 86%

location: 85, 12 | intruders visibility: 100 %| matching pixels: 76| matching pixels %: 86%

