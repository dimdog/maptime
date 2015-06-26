import csv

class capitolAPI:
  
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    with open(self.filename, 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      self.capitols = []
      for row in reader:
        self.capitols.append(row)
      
