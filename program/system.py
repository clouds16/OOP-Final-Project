from user import User
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from dbclass import DBUsers
from order import Order

class System:
    
    def __init__(self):
        self.userList = []
        self.currentUser = None
        self.currentOrder = Order()
        self.orderHistory = []
  
        
    
    def clearOrder(self):
        self.currentOrder = None
        self.currentOrder = Order()


    def createNewUser( self , userfname,  userlname , userphone,  useremail, userpw):
        user  = User(userfname , userlname , userphone , useremail , userpw)
        self.userList.append(user )
        self.currentUser = user

    
    def displayUsers(self):
        print(self.userList)

    def findUserByEmailAndPW(self, email, pw ):
        for i in self.userList:
            if i.email == email and i.password == pw:
                self.currentUser = i
                return i

        return None

    def findUserByEmail(self, email):
        for i in self.userList:
            if i.email == email:
                self.currentUser = i
                return i

        return None



    def loadDBUserByEmail(self, sql_engine, useremail):
        
        Session = sessionmaker(bind=sql_engine)
        session = Session()
        user = session.query(DBUsers).filter(DBUsers.email==useremail).first()
        self.currentUser = user
        return user


    def unloadUser(self):
        self.currentUser = None


    def completeOrder(self):
        self.orderHistory.append(self.currentOrder)
        self.currentOrder = Order()
####################################Integration Test ########################################
# newsystem = System()
# newsystem.createNewUser(  "hector" , "alvarez" , 805888888 , "hsemail@yahoo.com" , "thisissomepw" )
# newsystem.displayUsers()
