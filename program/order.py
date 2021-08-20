import datetime


class Order:
    def __init__(self):
        self.order_ID = None
        self.orderitems = []
        self.timestamp = datetime.datetime.now()
        self.tax = 0.095
        self.order_Total = 0

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

    def calculateTotal(self):
        for i in self.orderitems:
            try:
                self.order_Total += i.price  # all objects have a price variable
            except:
                print("Item has no price variable")

        # return sum of totals in order list * tax
        return self.order_Total * (1 + self.tax)

    def __repr__(self):
        return "{} {}".format(self.order_Total, self.orderitems)


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




