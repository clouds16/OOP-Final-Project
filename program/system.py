from user import User

class System:
    
    def __init__(self):
        self.userList = []
        self.currentUser = None

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

    def unloadUser(self):
        self.currentUser = None
####################################Integration Test ########################################
# newsystem = System()
# newsystem.createNewUser(  "hector" , "alvarez" , 805888888 , "hsemail@yahoo.com" , "thisissomepw" )
# newsystem.displayUsers()
