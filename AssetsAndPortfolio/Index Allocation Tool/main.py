import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
from flask import Flask
from flask import send_from_directory
import json as json
from flask import jsonify

#http://localhost:5000/index.html

files =	{
    "MSCI World.csv": 0.25,
    "MSCI EM.csv": 0.25,
    "MSCI Core Europe.csv": 0.25,
    "MSCI World Small Cap.csv": 0.25

}



def calc_json(files):
    df = pd.DataFrame()

    for file, weight in files.items():
        curDf = pd.read_csv(file, header=2, sep=',')
        curDf['Weight (%)'] *= weight
        df = df.append(curDf)


    countryWeight = df.groupby('Country')['Weight (%)'].sum().sort_values(ascending=False).round(2)
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
def hello_world():
    return calc_json(files)
# mimetype="application/json"

@app.route('/<path:path>')
def static_stuff(path):
    return send_from_directory('web', path)




if __name__ == "__main__":
    app.run(debug=True)
