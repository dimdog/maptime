import csv
import maptime.base as base
from sqlalchemy.ext.declarative import declarative_base
from collections import defaultdict

Base = declarative_base()

class DBPediaAPI:
  
  def __init__(self):
    self.connector = base.sqlConnection()

  def processRanks(self, ranks):
    for key, value in ranks:
      res = self.connector.session.query(base.Coordinates).filter(base.Coordinates.article == key).first()
      if res != None:
        res.rank = res.rank+value

    self.connector.session.commit()      
    self.connector.session.flush() 
    print "done updating this set..."

  def pageRank(self, linksFile):
    with open(linksFile, 'r') as ofile:
      header = ofile.readline()
      counter = 0
      for row in ofile.readlines(1000000):
        splits = row.split(" ")
        destination = splits[2].split("/")[-1][:-1]
        res = self.connector.session.query(base.Coordinates).filter(base.Coordinates.article == destination).first()
        if res != None:
          print res.article
          res.rank = res.rank+1
          counter+=1

        if counter==100:
          self.connector.session.commit()      
          self.connector.session.flush() 
          counter=0
          print "flushed"
      self.connector.session.commit()      
      self.connector.session.flush() 
      counter=0
      print "flushed"


  def load(self, coordinatesFile):
    errors = []
    with open(coordinatesFile, 'r') as ofile:
      counter = 0
      #articles = []
      for row in ofile.readlines():
        coordinateObj = base.Coordinates()
        article, syntax, lat, lng = row.split(" ")[:4]
        coordinateObj.article = u"%s"%article.split("/")[-1][:-1] # make it just the string at the end of the uri
        coordinateObj.lat = lat[1:]
        coordinateObj.lng = lng[:-1] 
        self.connector.session.add(coordinateObj)
        #articles.append(coordinateObj)
        counter+=1
        if counter==1000:
          print "1000"
          counter=0
          self.connector.session.flush()
          self.connector.session.commit()

    #self.loadErrors(errors,1000)
    print "flushing"
    self.connector.session.flush()
    print "commiting"
    self.connector.session.commit()
    print "done"

  def loadErrors(errors, limit):
    counter = 0 
    new_errors = []
    for row in errors:
        self.connector.session.add(coordinateObj)
        articles.append(coordinateObj)
        counter+=1
        if counter==limit:
          print limit
          counter=0
          try:
            self.connector.session.commit()
            self.connector.session.flush()
          except:
            errors.extend(articles) 
            articles = []
            self.connector.session.rollback()
            pass
      
    if limit >1:
      self.loadErrors(new_errors, limit-(limit/10)) 
    else:
      print new_errors

    self.connector.session.commit()
    self.connector.session.flush()
    



  def coord2Dict(self, coordinates):
    res = {}
    res = {
      'url': "http://en.wikipedia.org/wiki/%s"%(coordinates.article),
      'article' : coordinates.article,
      'lat': coordinates.lat,
      'lng': coordinates.lng
    }
    return res

  def query(self,swla,swln,nela,neln):
    res = self.connector.session.query(base.Coordinates).filter(base.Coordinates.lat > swla, base.Coordinates.lat < nela,
        base.Coordinates.lng > swln, base.Coordinates.lng < neln).order_by(base.Coordinates.rank.desc()).limit(50)
    response = []
    for row in res:
      response.append(self.coord2Dict(row)) 

    return response
    
      


