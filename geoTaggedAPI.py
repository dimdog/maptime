import csv

class GeoTaggedAPI:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    with open(self.filename, 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      self.articles = []
      for row in reader:
        lat,lng = row['location'].split(" ")
        trans = {
          "url" : row['wikipedia_article'],
          "lat" : lat,
          "lng" : lng
        }
        self.articles.append(trans)
      print self.articles[:5]
      print "done"
    
      

