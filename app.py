import os
import struct
import time
import capitolAPI
import geoTaggedAPI
import simplejson as json

from flask import Flask, Response, render_template, request

   
app = Flask(__name__)

api = capitolAPI.capitolAPI('data/capitols.csv')
api = geoTaggedAPI.GeoTaggedAPI('data/geoTaggedPartial.csv')

api.load()

@app.route('/years')
def dates():
  swla = request.args.get("swla")
  swln = request.args.get("swln")
  nela = request.args.get("nela")
  neln = request.args.get("neln")
  minimum = 23
  maximum = 5000
  return Response(json.dumps({'min' : minimum, 'max': maximum}), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 



@app.route('/data')
def data():
  print api.articles[:1]
  return Response(json.dumps(api.articles), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 


@app.route('/')
def root(): 
  return render_template('index.html')
    

if __name__ == '__main__':
  app.run(port=3000,host='0.0.0.0')



