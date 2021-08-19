import datetime


class Order:
    def __init__(self):
        self.order_ID = None
        self.order_items = []
        self.timestamp = datetime.datetime.now()
        self.tax = 0.095
        self.order_Total = 0

    def getOrderID(self):
        return self.order_ID

    def getTimeStamp(self):
        return self.timestamp

    def appendOrderItem(self, item):
        return self.order_items.append(item)

    def removeOrderItem(self, item):

        for index, i in enumerate(self.order_items):
            if i == item:
                self.order_items.remove(i)

    def calculateTotal(self):
        for i in self.order_Items:
            self.order_Total += i.price  # all objects have a price variable

        # return sum of totals in order list * tax
        return self.order_Total * (1 + self.tax)

    def __repr__(self):
        return "{} {}".format(self.order_Total, self.order_Items)
