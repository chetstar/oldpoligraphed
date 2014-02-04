PyClass_API_Project
===================
####
Project Overview
####
An open source web app for visualizing word frequency of political statements over time using the Sunlight Foundation API. The application will feature user logins and saved searches.

####
Roster
####
Cam
  Skills: Databases, Backend, Minor HTML/CSS

Jade
  Skills: Backend, logic, text parsing, Selenium - browser automation
  
John
  Skills: 
  
Jordan - Project Manager
  Skills: Front-End: HTML/CSS/Javascript. Python: Flask.
  
Nick
  Skills: Databases, Backend,

####
TODO
####
We know the project is finished when:
  A user can login, provide:
	  -search term
	  -date range
	  -boolean keywords or categories
  receives:
	  -graph
  can save:
	  -search

####
How to Run
####
Update pip_ and then setuptools

.. _pip: http://www.pip-installer.org/en/latest/installing.html

$ pip install --upgrade setuptools

If installation is a pain try this

$ pip install --allow-all-external --upgrade -r requirements.txt


#create and activate the venv

open the main app directory

$ virtualenv .

$ source bin/activate


#pip install the requirements

$ pip install -r requirements.txt --upgrade


#run the app

python run.py

go to http://127.0.0.1:5000/


####
API Key
####

To run this app you must have an api key from sunlight academy. 

Register: http://sunlightfoundation.com/api/accounts/register/

Create a apikey.py file under the src/app/ directory

Inside of the apikey.py file:

_API_KEY = '<your api key here>'