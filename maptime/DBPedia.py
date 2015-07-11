import csv
import maptime.base as base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBPediaAPI:
  
  def __init__(self, filename):
    self.filename = filename
    self.connector = base.sqlConnection()

  def load(self):

    
    with open(self.filename, 'r') as ofile:
      counter = 0
      for row in ofile.readlines():
        coordinateObj = base.Coordinates()
        article, syntax, lat, lng = row.split(" ")[:4]
        coordinateObj.article = article.split("/")[-1][:-1] # make it just the string at the end of the uri
        coordinateObj.lat = lat[1:]
        coordinateObj.lng = lng[:-1] 
        self.connector.session.add(coordinateObj)
        counter+=1
        if counter==10000:
          self.connector.session.commit()
          counter=0
          print "10000 more"

    self.connector.session.commit()
    print "done"

  def coord2Dict(self, coordinates):
    res = {}
    res = {
      'url': "http://en.wikipedia.org/wiki/%s"%(coordinates.article),
      'lat': coordinates.lat,
      'lng': coordinates.lng
    }
    return res

  def query(self,swla,swln,nela,neln):
    res = self.connector.session.query(base.Coordinates).filter(base.Coordinates.lat > swla, base.Coordinates.lat < nela,
        base.Coordinates.lng > swln, base.Coordinates.lng < neln).limit(50)
    response = []
    for row in res:
      response.append(self.coord2Dict(row)) 

    return response
    
      


