from flask import Flask, Response, send_from_directory, redirect, render_template, request, session, abort, Markup
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import datetime

app = Flask(__name__)

scheduler = BackgroundScheduler(daemon=True)
scheduler.start()
def importTask(timestamp):
    print(timestamp)
    # todo: call the method from DataImport.py
scheduler.add_job(importTask, 'interval', hours=12, args=[datetime.datetime.utcnow()])



@app.route('/data/<path:fileName>')
def seriesData(fileName):
    return send_from_directory('data', fileName)

@app.route('/data/indicators')
def indicatorsData():
    return send_from_directory('.', 'conf.json')

@app.route('/<page>', methods=["GET"])
def page(page):
    return render_template( page+'.html')


# Shutdown the cron thread if the web process is stopped
atexit.register(lambda: scheduler.shutdown(wait=False))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)