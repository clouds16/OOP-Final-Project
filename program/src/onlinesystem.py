from src.user import User 

class OnlineSystem :
    def __init__(self):
        self.userList = []

    
    def createNewUser( self, userfname, userlastname , userphone, useremail , userpassword) :
        self.userList.append( User(userfname, userlastname, useremail, userphone , userpassword))

    def findUserByEmail(self, email) :
        for i in self.userList :
            if i.email == email :
                return i

    def deleteUser(self , userEmail,  userPassword) :
        for i in self.userList:
            if i.email == userEmail and i.password == userPassword:
                self.userList.remove(i)



class System :
    def __init__(self):
        self.userList = []

    def createNewUser(self, userfname, userlname, userphone, useremail, userpassword) :
        self.userList.append( User(userfname , userlname , userphone , useremail , userpassword))
        