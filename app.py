import os
import struct
import time
import capitolAPI
import simplejson as json

from flask import Flask, Response, render_template, request

   
app = Flask(__name__)

api = capitolAPI.capitolAPI('data/capitols.csv')

api.load()




@app.route('/data')
def data():
  return Response(json.dumps(api.capitols), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 


@app.route('/')
def root(): 
  return render_template('index.html')
    

if __name__ == '__main__':
  app.run(port=3000,host='0.0.0.0')



