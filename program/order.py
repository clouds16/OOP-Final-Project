import datetime


class Order:
    def __init__(self):
        self.order_ID = None
        self.orderitems = []
        self.timestamp = datetime.datetime.now()
        self.tax = 0.095
        self.ordertotal = 0

    def getOrderID(self):
        return self.order_ID

    def getTimeStamp(self):
        return self.timestamp

    def appendOrderItem(self, item):
        self.orderitems.append(item)

    def removeOrderItem(self, item):
        for index, i in enumerate(self.orderitems):
            if i == item:
                self.orderitems.remove(i)

    def updateOrderTotal(self):
        price = 0
        for i in self.orderitems:
            price += i.price
            
        self.ordertotal = price # all objects have a price variable
        return self.ordertotal

    def calculateTotal(self):
        return self.ordertotal * (1 + self.tax)

    def __repr__(self):
        return "{} {}".format(self.ordertotal, self.orderitems)


# #<---- Order Class Tests ------->
# test = Order()

# #<----- Order append Item Test ------->
# test.appendOrderItem('Pizza')
# test.appendOrderItem('Pasta')
# test.appendOrderItem('Salad')
# print(test.orderitems)


# #<----- Remove Item Test ------->
# test.removeOrderItem('Pizza')
# test.removeOrderItem('Salad')
# test.removeOrderItem('Pizza')
# print(test.orderitems)


# #<----- Datetime Test ------->
# print(test.getTimeStamp())




