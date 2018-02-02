from flask import Flask, Response, send_from_directory
import pandas as pd


app = Flask(__name__, static_url_path='')

dateparse = lambda x: pd.datetime.strptime(x, '%m/%Y')
df = pd.read_csv('test.csv', sep='\t', parse_dates=['date'], date_parser=dateparse, thousands=',',
                 names=['date', 'assets'], index_col='date')
df['growth'] = (df['assets'] - df['assets'].shift())
df['growth_perc'] = (100 / df['assets'].shift() * df['growth'])
print(df)

@app.route('/data')
def hello_world():
    return Response(response=df.to_json(orient='split'), mimetype="application/json")

# Read for security reasons: https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
@app.route('/')
def serve_static():
    return send_from_directory('.', 'index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)