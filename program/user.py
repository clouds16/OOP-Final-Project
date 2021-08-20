from order import Order
from food import Pizzas , Pastas , Salads


class User: 
    def __init__ ( self, fname, lname,  phonenum , email, password) :
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.phonenum = phonenum
        self.__creditcard_num = None
        self.currentOrder = None
        self.Orders = []

    def createOrder(self):
        self.currentOrder = Order()
        
    
    def completeOrder(self):
        self.Orders.append(self.currentOrder)
        self.currentOrder = None
    
    def __repr__(self):
        return "<fname: {0} , lname: {1} , phone: {2} , email: {3} , pw: {4} >".format(self.fname, self.lname , self.phonenum , self.email , self.password)
################################  Integration Tests ###############################


# #menu items
# Pesto = Pizzas("Pesto", 12.99 , None , "pesto" , 12)
# Alfredo = Pastas("Alfredo" , 10.99 , "Angel Hair" , "Alfredo")  


# #create user
# Hector = User("Yogi" , "Bear" , "yogi@yahoo.com" , 888-420-6969)


# #create new order for user
# Hector.createOrder()
# print(Hector.currentOrder.getTimeStamp())
# #add items to order
# Hector.currentOrder.appendOrderItem(Pesto)
# Hector.currentOrder.appendOrderItem(Alfredo)
# #find cost
# cost = Hector.currentOrder.calculateTotal()
# print(cost)
# #finalize order
# Hector.completeOrder()
# print(Hector.Orders)
# #show that current order has been cleared and is ready for next order
# print("current order " , Hector.currentOrder)
# print("########################################")

# Hector.createOrder()
# Hector.currentOrder.appendOrderItem(Pesto)
# Hector.currentOrder.appendOrderItem(Alfredo)
# Hector.currentOrder.appendOrderItem(Pesto)
# Hector.currentOrder.appendOrderItem(Alfredo)
# Hector.currentOrder.appendOrderItem(Pesto)
# Hector.currentOrder.appendOrderItem(Alfredo)
# cost2 = Hector.currentOrder.calculateTotal()
# print("Price: ", cost2)
# Hector.completeOrder()
# print("current order: ",Hector.Orders)

