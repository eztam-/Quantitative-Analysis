#import matplotlib.pyplot as plt
#import numpy as np

import pandas as pd
from flask import Flask
from flask import send_from_directory
import json as json
from flask import jsonify

#http://localhost:5000/index.html

files =	{
    "MSCI_Europe.csv": 0.25,
   # "MSCI_USA_Equal_Weight.csv": 0.25,
    "MSCI_EM_small_cap.csv": 0.25,
    "MSCI_EM.csv": 0.25,
    "MSCI_Eastern_Europe.csv": 0.25,
 #   "MSCI_Pacific_ex_japan.csv":10

}






def calc_json(files):
    df = pd.DataFrame()

    for file, weight in files.items():
        curDf = pd.read_csv(file, header=2, sep=',')
        curDf['Weight (%)'] *= weight
        df = df.append(curDf)


    countryWeight = df.groupby('Location')['Weight (%)'].sum().sort_values(ascending=False).round(2)
    ccyWeight = df.groupby('Market Currency')['Weight (%)'].sum().sort_values(ascending=False).round(2)
    sectorWeight = df.groupby('Sector')['Weight (%)'].sum().sort_values(ascending=False).round(2)
    instumentWeight = df[df.ISIN != '-'].groupby('Name')['Weight (%)'].sum().sort_values(ascending=False).round(2)

    print(countryWeight)

    print(df['Weight (%)'].sum())

    x = {
        "country": countryWeight.to_dict(),
        "ccy": ccyWeight.to_dict(),
        "sector": sectorWeight.to_dict(),
        "instrument": instumentWeight.to_dict()
    }

    print(json.dumps(x))
    #return json.dumps(x)
    return jsonify(x)




app = Flask(__name__)
@app.route('/data.json')
def data():
    return calc_json(files)


@app.route('/<path:path>')
def static_stuff(path):
    return send_from_directory('web', path)

@app.route('/')
def index():
    return send_from_directory('web', 'index.html')


if __name__ == "__main__":
    app.run(debug=True)
