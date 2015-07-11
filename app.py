import os
import struct
import time
import maptime.DBPedia as DBPedia
import simplejson as json

from flask import Flask, Response, render_template, request

   
app = Flask(__name__)

DBPediaApi = DBPedia.DBPediaAPI('data/coordinates.nt')


@app.route('/data')
def data():
  swla = request.args.get("swla")
  swln = request.args.get("swln")
  nela = request.args.get("nela")
  neln = request.args.get("neln")
  return Response(json.dumps(DBPediaApi.query(swla,swln,nela,neln)), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 





@app.route('/')
def root(): 
  return render_template('index.html')
    

if __name__ == '__main__':
  app.run(port=3000,host='0.0.0.0')



