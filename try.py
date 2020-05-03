import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datefinder
from datetime import datetime, timedelta
import pandas as pd
# If modifying these scopes, delete the file token.pickle.
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
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
else:
    flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
    creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

service = build("calendar", "v3", credentials=creds)
def create_events(start_time_str, summary, duration=1,attendees=None, description=None, location=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    dicto={}
    print(attendees)
    t=[]
    for i in attendees:
            #dicto['email']=i
            t.append({'email':i})
    print(dicto)
    print(t)
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },

        'attendees': t,
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
        ],
        'recurrence': [
            'RRULE:FREQ=WEEKLY;UNTIL=20200430T240000Z',
        ]
    }

    return service.events().insert(calendarId='primary', body=event,sendNotifications=True).execute()

df=pd.read_csv("Final Calendar Invites to be sent.csv")
print(df)
concat=df["Email"]
#create_events('11 April 1.00pm', 'Codepth:Testing Reminder',1,list(concat))
team_for_invite="Data Science"
#create_events('11 April 5.00pm', 'Looking at the Sentrifugo profile',.2,list(concat),'Make sure the profiles at the Sentrifugo are completed','https://hrm.codepth.com/index.php/')

'''if team_for_invite=="Content and Media":
    k= df[df["Department"]=='Content and Media']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])

    print(concat["Email"])
    emails=concat["Email"]
    create_events('17 April 10.00pm', 'Codepth:Content Team Weekly Meeting 10:00Pm-11:00PM',1,list(emails))
'''
'''
if team_for_invite=="Web Technology":
    k= df[df["Department"]=='Web Technology']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])

    print(concat["Email"])
    emails=concat["Email"]
    create_events('14 April 11.00pm', 'Codepth:Web Team Weekly Meeting 11:00Pm-12:00PM',1,list(emails))

'''
'''
if team_for_invite =="Design and Creative":
    k= df[df["Department"]=='Design and Creative']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])
    print(concat["Email"])
    emails=concat["Email"]
    create_events('12 April 9.00pm', 'Codepth:Design and Creative Team Weekly Meeting 9:00Pm-10:00PM',1,list(emails))
'''
'''
if team_for_invite =="Mobile Technology":
    k= df[df["Department"]=='Mobile Technology']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])
    print(concat["Email"])
    emails=concat["Email"]
    try:
        create_events('11 April 11.00pm', 'Codepth:Mobile Technology Team Weekly Meeting 10:00Pm-11:00PM',1,list(emails))
    except:
        print("Request limit exceded")
        create_events('11 April 11.00pm', 'Codepth:Mobile Technology Team Weekly Meeting 10:00Pm-11:00PM',1,list(emails))
'''
'''
if team_for_invite =="Sales and Marketing":
    k= df[df["Department"]=='Sales and Marketing']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])
    print(concat["Email"])
    emails=concat["Email"]
    create_events('14 April 10.00pm', 'Codepth:Sales and Marketing Team Weekly Meeting 10:00Pm-11:00PM',1,list(emails))
'''
'''
if team_for_invite =="Human Resources":
    k= df[df["Department"]=='Human Resources']
    y=df[df["Department"]=='CEO']
    print(y)
    k.append(y)
    #print()
    concat=pd.concat([k,y])
    #k= df[df["Department"]=='Operations']
    print(k)
    #contact=pd.concat([k,concat])
    print(concat["Email"])
    emails=concat["Email"]
    create_events('12 April 10.00pm', 'Codepth:HR & Operations Team Weekly Meeting 10:00Pm-11:00PM',1,list(emails))

'''
if team_for_invite =="Data Science":
    k= df[df["Department"]=='Data Science']
    #y=df[df["Department"]=='CEO']
    #print(y)
    #k.append(y)
    #print()
    #concat=pd.concat([k,y])
    #k= df[df["Department"]=='Operations']
    #print(k)
    #contact=pd.concat([k,concat])
    concat=k
    print(concat["Email"])
    emails=concat["Email"]
    create_events('13 April 9.10pm', 'Codepth:Data Science Team Weekly Meeting 9:00Pm-10:00PM',1,list(emails))

#create_events('6 April 1.00pm', 'Deloitte Start time',0.5,'ekansh031998@gmail.com')
#Recurrence -'recurrence': [
#    'RRULE:FREQ=WEEKLY;UNTIL=20200615T240000Z',
#  ],
