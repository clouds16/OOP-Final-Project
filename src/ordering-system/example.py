from Food import Pizzas,Pastas, Salads

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

    def addSalad(self):
        pass

    def removeSalad(self):
        pass

    def addPasta(self):
        pass

    def removePasta(self):
        pass
    
    def addBeverage(self):
        pass

    def removeBeverage(self):
        pass

################################  Integration Tests ###############################

new_menu = Menu()
#Adding Pizza using the adding_pizza
new_menu.addPizza('pepporoni',12.99)
new_menu.addPizza('cheese', 12.99)
new_menu.addPizza('apple', 12.99)
new_menu.addPizza('tomato', 12.99)

#Finding the position 
print(new_menu.findPosition('tomato'))
print(new_menu.menu_items)
new_menu.removePizza('button')
print(new_menu.menu_items)


# class Beverages():
#     def __init__(self, price, size, name):
#         self.price = price
#         self.size = size
#         self.name = name

    


# class Customer():
#     def __init__(self,customerID,customerName,customerPhoneNumber,customerEmailAddress,customerAddress,customerZipCode):
#         self.customerID = customerID
#         self.customerName = customerName
#         self.customerPhoneNumber = customerPhoneNumber
#         self.customerEmailAddress = customerEmailAddress
#         self.customerAdress = customerAddress
#         self.customerZipCode = customerZipCode


#     def login(self):
#         pass

#     def logout(self):
#         pass

#     def makePayment(self):
#         pass

#     def addInfo(self):
#         pass

#     def editInfo(self):
#         pass

#     def createOrder(self):
#         pass


# class Employee():
#     def __init__(self,employeeID,employeeName,employeePhone,employeeShift,employeeSchedule):
#         self.employeeId = employeeID
#         self.employeeName = employeeName
#         self.employeePhone = employeePhone
#         self.employeeShift = employeeShift
#         self.employeeSchedule = employeeSchedule


#     def workLogin(self):
#         pass

#     def workLogOut(self):
#         pass

#     def payEmployee(self):
#         pass

#     def deliverPizza(self):
#         pass
