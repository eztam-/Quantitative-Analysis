from pandas_datareader import data, wb
import pandas as pd
import datetime
import os.path
import json

def fetchData(symbol, start, invert=False):
    series = data.DataReader(symbol, "fred", start, datetime.datetime.now())
    return series if not invert else series.applymap(lambda x: 1/x)

def update_data_series(seriesId, dataSource, start, invert=False):
    fileName = 'data/'+dataSource+'_'+seriesId+'.json'
    fromNet = fetchData(seriesId, start, invert)
    if os.path.isfile(fileName):
        fromFile = pd.read_json(fileName, orient="split")
        fromFile.update(fromNet)
        fromNet = fromFile.combine_first(fromNet)
    fromNet.to_json(fileName, orient="split")


with open('conf.json') as data_file:
    conf = json.load(data_file)
    for series in conf:
        print('Importing series: '+series['id'])
        start = datetime.datetime.strptime(series['start'], '%Y-%m-%d')
        if series['source'] == None: continue
        update_data_series(series['id'], series['source'], start)



#update_data_series('DEXSZUS', 'fred', START)
#print(pd.read_json('fred_DEXSZUS.json', orient="split"))


