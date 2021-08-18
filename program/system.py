from user import User

class System:
    
    def __init__(self):
        self.userList = []

    def createNewUser( self , userfname,  userlname , userphone,  useremail, userpw):
        user  = User(userfname , userlname , userphone , useremail , userpw)
        self.userList.append(user )

    
    def displayUsers(self):
        print(self.userList)


####################################Integration Test ########################################
# newsystem = System()
# newsystem.createNewUser(  "hector" , "alvarez" , 805888888 , "hsemail@yahoo.com" , "thisissomepw" )
# newsystem.displayUsers()
