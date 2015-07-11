print "heree"
import os
import time
import maptime.DBPedia as DBPedia
import simplejson as json
import wikipedia

from flask import Flask, Response, render_template, request

   
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


#DBPediaApi = DBPedia.DBPediaAPI('data/coordinates.nt', 'data/page_links/page_links_en.nt')

#DBPediaApi.load()

#DBPediaApi.pageRank()


@app.route('/data')
def data():
  swla = request.args.get("swla")
  swln = request.args.get("swln")
  nela = request.args.get("nela")
  neln = request.args.get("neln")
  #return Response(json.dumps(DBPediaApi.query(swla,swln,nela,neln)), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 
  #return Response(json.dumps("hello"),swln,nela,neln)), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 

@app.route('/wiki')
def articles():
  article_name = request.args.get("article")
  article =  wikipedia.search(article_name)[0]
  article = wikipedia.page(article)
  res = {
    'title' : article.title,
    'content' : article.content
  }
  return Response(json.dumps(res), mimetype="application/json", headers= {"Access-Control-Allow-Origin":"*", "Content-Type":"application/json"}) 




@app.route('/')
def root(): 
  return render_template('index.html')
    



