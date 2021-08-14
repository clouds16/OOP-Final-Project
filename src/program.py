import math as m

class Food:
    def __init__(self, name, price ):
        self.name = name 
        self.price = price
        
        
    tax = .10

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def orderTotal(self):
        return (self.price + self.price*self.tax)


class Pizzas(Food):
    def __init__(self, pizza_name, pizza_price, toppings, sauce, size) :
        self.toppings = toppings
        self.sauce = sauce 
        self.size = size
        super().__init__( pizza_name , pizza_price )

    def getToppings(self):
        return [i for i in self.toppings]

    def getArea(self):
        return (m.pi/4)* self.size**2

    def __repr__(self) :
        return "{0} {1} {2}".format(self.toppings, self.sauce, self.size)


class Salads(Food):
    def __init__(self, salad_name,  salad_price ,  dressing, size  ) :
        self.dressing = dressing
        self.size = size
        super().__init__( salad_name, salad_price)
    
    def getDressing(self):
        return self.dressing
    
    def getSize(self):
        return self.size



class Pastas(Food):
    def __init__(self , pasta_name, pasta_price, noodles , sauce ):
        self.noodles = noodles
        self.sauce = sauce
        super().__init__(pasta_name, pasta_price)

    def getNoodleType(self):
        return self.noodles
    
    def getSauce(self):
        return self.sauce
    #comment


    #changes