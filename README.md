# NOTES APP

## About the project 
The notes app project is a Python based REST project, that allows authenticated users to Create, Read , Update and Delete Notes in the application. It uses Django Rest Framework to create REST APIs.
It uses the following :
- Python version - 3.10
- Django version - 5.0.2
- Django Rest Framework - 3.14.0

#### All dependencies can be installed with the requirements.txt file

## Features Present :
 - User Login
 - User Sign-in
 - Adding New Note
 - Getting All Notes
 - Getting a specific note by ID,
 - Get all the versions of a specific note


## API Endpoints :

The application runs on the port : `http://127.0.0.1:8000/`

Endpoints  : 
 - `http://127.0.0.1:8000/login` - Request Type : `POST`. Shows a login screen to authenticate a user, after which the user can create notes.
 - `http://127.0.0.1:8000/signup` - Request Type : `POST`. Shows a signup screen to authenticate a user, after which the user can create notes.
 - `http://127.0.0.1:8000/notes` - Request Type : `GET`. Fetches all the notes stored by the user in the DB. If the user has no notes, it returns an empty query set.

 - `http://127.0.0.1:8000/notes/create` - Request Type : `POST`. Allows a Logged-in user to create a new note and store it in the DB. Format to add new note :
 
     Sample request to create a new note :
   
     Properties : 
     * title : Title of the note
     * content : Content of the note
     * version [optional]: version of the note
     * priority attribute has options :
        H = High
        M = Medium
        L = Low
   ```   
     without adding version : 
      {
          "title":"Your title",
          "content":"The content of your note",
          "priority":"H"
     }
     
     with user preferred version : 
       {
          "title":"Your title",
          "content":"The content of your note",
          "version" : 0
          "priority":"H"
     }
     
     ```
 - `http://127.0.0.1:8000/notes/{id}` - Request Type : `GET`. Fetches a specific not based on the given ID, if the ID is not present, then it shows a `400` status with `BAD REQUEST` message.
 - `http://127.0.0.1:8000/notes/update/{id}` - Request Type : `PATCH`. Allows an authenticated user to ipdate a specific not based on its ID. If the ID is invalid, it shows a `400` status with `BAD REQUEST` message.
    Sample Update request : 
    ```
     {
          "title":"Your updated title",
          "content":"The updated content of your note",
          "priority":"updated option"
     }
   ```
   The version, if not updated by the user manually, will automatically update the value.
 - `http://127.0.0.1:8000/notes/delete` - Request Type : `DELETE`. Deletes all the notes that an authenticated user has created. Returns a `Success` message on successful delete.
 - `http://127.0.0.1:8000/notes/delete/{id}` -  Request Type : `DELETE`. Deletes a note with a specific ID. If the ID is not present, it will send a `400` status response with a message.
 - `http://127.0.0.1:8000/notes/versions` - Request Type : `GET`. Fetches all the versions of all the notes the authenticated user has created.
 - `http://127.0.0.1:8000/notes/versions/{id}` - Request Type : `GET`. Fetches all the versions of a note having a specific ID. If the ID is present it returns the list of version changes. Other-wise it returns a `400` status with a message.
 - 


## How to run the application in you local system :
Before you run the application , make sure to execute the `pip install requirements.txt` command to install all dependencies.

You can run the server using the ` python3 manage.py runserver` command. The application will run at 
http://127.0.0.1:8000/
