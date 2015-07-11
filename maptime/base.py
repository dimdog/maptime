import random
from sqlalchemy import String, Float, Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class sqlConnection:

  def __init__(self):
    self.engine = self.get_engine()
    self.session = self.make_session(self.engine)

  def get_engine(self):
    return create_engine("postgres://dlgrtxciercfic:o5jStUy_qsVtULfOTMHpDbcS1O@ec2-107-22-175-206.compute-1.amazonaws.com:5432/dbj3fpv0kh4auk")

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
    rank = Column(Integer, default=0)
    
    
    


  
#create table coordinates ( id SERIAL, article VARCHAR(255) not null, lat FLOAT not null, lng FLOAT not null, rank INTEGER not null default 0, primary key (id) );
