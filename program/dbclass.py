
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload

Base = declarative_base()

class DBUsers(Base):
    __tablename__ = 'users'
    fname = Column(String)
    lname = Column(String)
    phone = Column(String)
    email = Column(String , primary_key= True)
    password = Column(String)

    def __repr__(self):
       return "<fname: {0} , lname: {1} , phone: {2} , email: {3} , password: {4}>"\
           .format(self.fname, self.lname , self.phone , self.email , self.password)