
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    email = Column(String(100))
    created_on = Column(DateTime, default=datetime.now)

class Chart(Base):
    __tablename__ = "charts"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    path = Column(String(255))
    created_on = Column(DateTime, default=datetime.now)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    created_at = Column(DateTime, default= datetime.now)
    
class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    path = Column(String)
    created_at = Column(DateTime, default= datetime.now)
    
class Analysis(Base):
    __tablename__ = "analysis"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    path = Column(String)
    data_source_id = Column(Integer, ForeignKey('datasets.id'))
    created_at = Column(DateTime, default=datetime.now())

# utility functions
def get_db():
    engine = create_engine('sqlite:///apad.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

def save_to_db(object):
    db = get_db()    
    db.add(object)
    db.commit()
    db.close()

# create database
if __name__ == "__main__":
    engine = create_engine('sqlite:///apad.db')
    Base.metadata.create_all(engine)