# DAP
A Patient Data management and processing platform

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the DAP folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**


## Login

The login page is common for clients and Hospitals.  
The username is their name and password for everyone is 'project123'.  

Example usernames:  
user1- 'samarth'  
user2- 'trisila'  

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'admin' and the above password.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New clients and hospitals can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Client, Hospital, Medical_History, Current_State, etc.

**For more details regarding the system and features please refer the reports included.**
