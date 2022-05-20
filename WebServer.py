import time
import flask
from flask import Flask
import requests
import json
from threading import Thread

app = Flask(__name__)
def GetRoliValues():
    global data
    while True:
        try:
            r = requests.get("https://www.rolimons.com/itemapi/itemdetails")
            print(r.status_code)
            print(r.headers)
            print(r.cookies)
            #print(json.loads(r.text))
            if r.status_code == 200:
                data = flask.Response(r.text)
                time.sleep(65)
        except Exception as e:
            print(e)

@app.route('/')
def example():
    global data
    data.headers['Access-Control-Allow-Origin'] = 'https://www.roblox.com'
    return data

Thread(target=GetRoliValues).start()

if __name__ == '__main__':
    app.run(host="0.0.0.0")