from src.food import Pastas, Pizzas , Salads , Beverages

class Menu:
    def __init__(self):
        self.restaurant_name = ''
        self.menu_items = []
        self.isDiscount = None

    def addPizza(self,name,price):
        new_pizza = Pizzas(name,price)
        self.menu_items.append(new_pizza)
        
    def removePizza(self,name):
        for i in self.menu_items:
            if i.pizza_name == name:
                self.menu_items.remove(i)
    
    def findPosition(self,name):
        for index,i in enumerate(self.menu_items):
            if i.pizza_name == name:
                return index

    def addSalad(self,name,price,dressing,size):
        new_salad = Salads(name,price,dressing,size)
        self.menu_items.append(new_salad)

    def removeSalad(self,name):
        for i in (self.menu_items):
            if i.name == name:
                self.menu_items.remove(i)

    def addPasta(self,name,price,noodles,sauce):
        new_pasta = Pastas(name,price,noodles,sauce)
        self.menu_items.append(new_pasta)

    def removePasta(self,name):
        for i in (self.menu_items):
            if i.name == name:
                self.menu_items.remove(i)

    def addBeverage(self,name,price):
        new_beverage = Beverages(name,price)
        self.menu_items.append(new_beverage)

    def removeBeverage(self,name):
        for i in (self.menu_items):
            if i.name == name:
                self.menu_items.remove(i)
    
    def getItem(self,name):
        for i in self.menu_items:
            if i.name == name:
                return i




# ################################  Integration Tests ###############################

# new_menu = Menu()
# #Adding Pizza using the adding_pizza
# new_menu.addPizza('pepporoni',12.99)
# new_menu.addPizza('cheese', 12.99)
# new_menu.addPizza('apple', 12.99)
# new_menu.addPizza('tomato', 12.99)
# #<---- End Of Pizzas Test ----------->


# #Finding the position 

# print(new_menu.findPosition('tomato'))
# print(new_menu.menu_items)

# #Testing with item not included in the list
# new_menu.removePizza('button')
# print(new_menu.menu_items)
# #<---- End Of Finding Position ----------->

# #Testing Salad class
# new_menu.addSalad('cesar',10.99,'cesar','s')
# print(new_menu.menu_items)
# new_menu.removeSalad('cesar')
# print(new_menu.menu_items)

# #<---- End Of Salads Test ----------->

# #Testing Pasta
# new_menu.addPasta('Little Italy', 13.99, 'Linguine','Marinara')
# print(new_menu.menu_items)
# new_menu.removePasta('Little Italy')
# print(new_menu.menu_items)
# #<---- End Of Pastas Test ----------->


# #Testing Beverages
# new_menu.addBeverage('Pepsi',1.99)
# print(new_menu.menu_items)
# new_menu.removeBeverage('Pepsi')
# print(new_menu.menu_items)

# #<---- End Of Beverages Test ----------->

# #Testing GetItem 
# print(new_menu.getItem('pepporoni'))
# print(new_menu.getItem('cheese'))

# #<---- End Of GetItem Test ----------->

