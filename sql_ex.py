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

def extract():
    # ex = start()
    # engine = ex.engine
    # start(engine = engine)
    engine = db.create_engine('sqlite:///records.sqlite')
    connection = engine.connect()
    metadata = db.MetaData()
    rcd = db.Table('rcd', metadata, autoload=True, autoload_with=engine)
    query = db.select([rcd])
    ResultProxy = connection.execute(query)
    results = ResultProxy.fetchall()
    df = pd.DataFrame(results)
    df.columns = results[0].keys()
    connection.invalidate()
    engine.dispose()
    df1 = pd.DataFrame(df)
    # df1.columns = df[0].keys()
    # print(df1)
    return df1
# extract()
