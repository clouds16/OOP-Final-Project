
class User: 

    def __init__ ( self, fname, lname, email, phonenum) :
        self.fname = fname
        self.lname = lname
        self.__email = email
        self.__phonenum = phonenum
        self.__creditcard_num = None
        
        self.currentOrder = None
        self.Orders = []


    def createOrder(self, Item):
        #newOrder = Order()
        self.currentOrder = Item
        pass
    
    def completeOrder(self):
        self.Orders.append(self.currentOrder)
        self.currentOrder = None
    



newUser = User("hector", "alvarez", "hect16@gmail.com", 8057177738)
newUser.createOrder("string")
print(newUser.currentOrder)

