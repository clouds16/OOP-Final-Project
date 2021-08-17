
import datetime

class Order:
    def __init__(self ):
        #self.orderID = orderID
        self.orderItems = []
        self.timestamp = datetime.datetime.now()
        self.tax = 0.095
        self.orderTotal = 0
        
    # def getOrderID(self):
    #     return self.orderID

    def getTimeStamp(self):
        return self.timestamp

    def appendOrderItem(self , item) :
        try:
            self.orderItems.append(item)
        except :
            raise ValueError('Could not append item') 

    def removeOrderItem(self, item ):
        try :
            pass
        except :
            raise ValueError('Could not remove item')

    def calculateTotal(self):
        for i in self.orderItems:
            self.orderTotal += i.price #all objects have a price variable 
        
        return self.orderTotal* (1 + self.tax) #return sum of totals in order list * tax
    
            
    def __repr__(self) :
        return "{} {}".format(self.orderTotal , self.orderItems)
