from User import User 

class OnlineSystem :
    def __init__(self):
        userList = []

    def createNewUser(self, fname, lname , phone, email , password) :
        
        self.userList.append(User(fname, lname, email, phone , password))

    def findUserByEmail(self, email) :
        for i in self.userList :
            if i.email == email :
                return i

    def deleteUser(self , userEmail,  userPassword) :
        for i in self.userList:
            if i.email == userEmail and i.password == userPassword:
                self.userList.remove(i)