import sqlalchemy as db
import pandas as pd
from datetime import datetime

class DataBase:
    def __init__(self):
        engine = db.create_engine('sqlite:///records.sqlite') #Create test.sqlite automatically
        connection = engine.connect()
        metadata = db.MetaData()

        rcd = db.Table('rcd', metadata,
                      #db.Column('Id', db.Integer()),
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
        #Inserting record one by one
        # query = db.insert(rcd).values(Id=1, name='naveen', salary=60000.00, active=True)
        # ResultProxy = connection.execute(query)
        self.engine = engine
        self.rcd = rcd

def start():
    return DataBase()

def maintain(summary,date,start_time,end_time,email_list,description="None",location="None",response="None"):
    ex = start()
    rcd = ex.rcd
    engine = ex.engine
    now = datetime.now()
    query = db.insert(rcd)
    data = [{
        'Summary':summary,
        'Meeting_Date':date,
        'Start_Time':start_time,
        'End_Time':end_time,
        'Invitees' : email_list,
        'Description' : description,
        'Location' : location,
        'Record_Date' : now.strftime("%B %d, %Y"),
        'Record_Time' : now.strftime("%H:%M:%S"),
        'Response':response,
    }]
    connection = engine.connect()
    # metadata = db.MetaData()
    ResultProxy = connection.execute(query,data)
    # status.connection.execute(query,data)
    # ResultProxy = connection.execute(query)
    return

def extract():
    ex = start()
    engine = ex.engine
    # start(engine = engine)
    # db.create_engine('sqlite:///records.sqlite')
    connection = engine.connect()
    metadata = db.MetaData()
    rcd = db.Table('rcd', metadata, autoload=True, autoload_with=engine)
    query = db.select([rcd])
    ResultProxy = connection.execute(query)
    results = ResultProxy.fetchall()
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    df1 = pd.DataFrame(df)
    # df1.columns = df[0].keys()
    # print(df1)
    return df1
# extract()
