import random
from maptime import config
from sqlalchemy import String, Float, Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class sqlConnection:

  def __init__(self):
    self.engine = self.get_engine()
    self.session = self.make_session(self.engine)

  def get_engine(self):
    test = config.get('test')
    sqla_url = config.get('sqlalchemy.url')
    username = config.get('sqlalchemy.username')
    password = config.get('sqlalchemy.password')
    host = config.get('sqlalchemy.host')
    database = config.get('sqlalchemy.database')
    
    return create_engine(sqla_url%(username,password,host,database))

  def make_session(self, engine):
    session = Session(engine)
    session.connection()
    return session


class Coordinates(Base):
    __tablename__ = 'coordinates'
    id = Column(Integer, primary_key=True)
    article = Column(String)
    lat = Column(Float, index=True)
    lng = Column(Float, index=True)
    
    
    



  

