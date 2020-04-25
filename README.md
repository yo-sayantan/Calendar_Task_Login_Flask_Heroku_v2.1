# Calendar Add Task Flask App
This is a demo project to elaborate how tasks can be added to a calendar and events can be registered in Google Calendar and send invites to paricipants using Flask API & Google Calendar API

## Prerequisites
You must have Scikit Learn, numpy, google_auth_oauthlib, rfc3339, datetime and Flask (for API) installed.

## Project Structure
This project has four major parts :
1. app.py - This contains Flask APIs that receives al the required details through GUI or API calls, and calls the util.py for running the Python code responsible for event registration and sending invites.
3. util.py - The gets the Google authorisation tokens from Google server and uses the token to access the calendar for event booking and sending invites.
4. templates - This folder contains the HTML template to allow user to enter all the details like date, summary, start & end time, invitees enail address etc like a generalised UI. Finally it shows confirmation message at the bottom.

### Running the project
1. Run app.py using below command to start Flask API
```
python3 app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

THANK YOU
