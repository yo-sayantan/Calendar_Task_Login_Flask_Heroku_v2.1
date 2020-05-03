##################################################
## Author: {Sayantan Biswas}
## Maintainer: {Sayantan Biswa}
## Email: {sayantanbiswas1002@gmail.com}
##################################################


#!/usr/bin/python3.4
import sqlalchemy as db
import pandas as pd
from datetime import datetime
from sqlalchemy.sql import text

class DataBase:
    def __init__(self):
        engine = db.create_engine('sqlite:///records.sqlite') #Create test.sqlite automatically
        connection = engine.connect()
        metadata = db.MetaData()

        rcd = db.Table('rcd', metadata,
                      db.Column('Summary', db.String(255)),
                      db.Column('Meeting_Date', db.String(255)),
                      db.Column('Start_Time', db.String(255)),
                      db.Column('End_Time', db.String(255)),
                      db.Column('Invitees', db.String(25500)),
                      db.Column('Description', db.String(255)),
                      db.Column('Location', db.String(255)),
                      db.Column('Record_Date', db.String(255)),
                      db.Column('Record_Time', db.String(255)),
                      db.Column('Response', db.String(25500)),
                      )

        metadata.create_all(engine) #Creates the table
        # return engine,rcd
        # Inserting record one by one
        # query = db.insert(rcd).values(Id=1, name='naveen', salary=60000.00, active=True)
        # ResultProxy = connection.execute(query)
        self.engine = engine
        self.rcd = rcd

def start():
    return DataBase()

def maintain(summary,date,start_time,end_time,email_db,description="None",location="None",response="None"):
    ex = start()
    # start(engine = engine)
    rcd = ex.rcd
    engine = ex.engine
    now = datetime.now()
    query = db.insert(rcd)
    email_list_final=[]
    email_list_final = str(email_db)
    data = [{
        'Summary':summary,
        'Meeting_Date':date,
        'Start_Time':start_time,
        'End_Time':end_time,
        'Invitees' : email_list_final,
        'Description' : description,
        'Location' : location,
        'Record_Date' : now.strftime("%B %d, %Y"),
        'Record_Time' : now.strftime("%H:%M:%S"),
        'Response': response,
    }]
    # data = (summary,date,start_time,end_time,str(email_list),description,location,now.strftime("%B %d, %Y"),now.strftime("%H:%M:%S"),response)
    # query = "INSERT INTO rcd (Summary,Meeting_Date,Start_Time,End_Time,Invitees,Description,Location,Record_Date,Record_Time,Response) VALUES (data)"
    # query = text("""INSERT INTO rcd(Summary, Meeting_Date, Start_Time, End_Time, Invitees, Description, Location, Record_Date, Record_Time, Response)
            # VALUES(:Summary, :Meeting_Date, :Start_Time, :End_Time, :Invitees, :Description, :Location, :Record_Date, :Record_Time, :Response)""")

    connection = engine.connect()
    # metadata = db.MetaData()
    # data = unicode(data)
    ResultProxy = connection.execute(query,data)
    # for line in data:
    #     connection.execute(query, **line)
    # status.connection.execute(query,data)
    # ResultProxy = connection.execute(query)
    connection.invalidate()
    engine.dispose()
    return
