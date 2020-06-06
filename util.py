##################################################
## Author: {Sayantan Biswas}
## Maintainer: {Sayantan Biswa}
## Email: {sayantanbiswas1002@gmail.com}
##################################################


#!/usr/bin/python3.4
import json, pickle
import numpy as np
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datefinder
from datetime import datetime, timedelta
from rfc3339 import rfc3339

SCOPES = ['https://www.googleapis.com/auth/calendar']
timezone = 'Asia/Kolkata'
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
else:
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build("calendar", "v3", credentials=creds)

def add_event(summary,date,start_time,end_time,email_list,description=None,location=None):
    matches = list(datefinder.find_dates(start_time))

    if len(matches):
        start = matches[0]
    matches = list(datefinder.find_dates(end_time))
    if len(matches):
        end = matches[0]

    start = rfc3339(start)
    end = rfc3339(end)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start, #_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },

        'end': {
            'dateTime': end, #_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },

        'attendees': email_list,

        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()
    return('Event created: %s' %(event.get('summary'))+' for %s' %(event.get('description')))

if __name__ =="__main__":
    print("Starting python Flask server...")
    # util.load_saved_artifacts()
    app.run(debug=True)
