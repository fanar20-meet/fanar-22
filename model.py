from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    year= Column(String)
    num =Column(Integer)


    def __repr__(self):
        return ("User Name: {}\n"
                "User Year: {} \n").format(
                    self.name,
                    self.year)



