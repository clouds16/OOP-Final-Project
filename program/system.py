from user import User

class System:
    
    def __init__(self):
        self.userList = []

    def createNewUser( self , userfname,  userlname , userphone,  useremail, userpw):
        user  = User(userfname , userlname , userphone , useremail , userpw)
        self.userList.append(user )

    
    def displayUsers(self):
        print(self.userList)

    def findUserByEmailAndPW(self, email, pw ):
        for i in self.userList:
            print(i)
            if i.email == email and i.password == pw:
                return i

        return None

    def findUserByEmail(self, email):
        for i in self.userList:
            print(i)
            if i.email == email:
                return i

        return None

####################################Integration Test ########################################
# newsystem = System()
# newsystem.createNewUser(  "hector" , "alvarez" , 805888888 , "hsemail@yahoo.com" , "thisissomepw" )
# newsystem.displayUsers()
