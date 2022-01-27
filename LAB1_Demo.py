#Create Class
class Employee:
	def __init__(self, name, position, address, tel):
        self.Name = name
    	self.Position = position
    	self.Address = address
    	self.Tel = tel
 
class Customer:
	def __init__(self, name, address, tel, discount):
    	self.Name = name
    	self.Address = address
    	self.Tel = tel
    	self.Discount = discount
 
class Cake:
	def __init__(self, amount, price):
    	self.Amount = amount
    	self.Price = price
 
class Brownie:
	def __init__(self, amount, price):
    	self.Amount = amount
    	self.Price = price
 
class Cookie:
	def __init__(self, amount, price):
    	self.Amount = amount
    	self.Price = price
 
class Bun:
	def __init__(self, amount, price):
    	self.Amount = amount
    	self.Price = price
 
class Macarons:
	def __init__(self, amount, price):
    	self.Amount = amount
    	self.Price = price


#-------------Instance & Class-------------
Employee_Manager = Employee("Suwitcha Dathong", "Menager", "Bangkok", "089-898-9898")
Customer_00 = Customer("Unnop Thamtiengtham", "Bangkok", "099-745-5348", 5)
Cake = Cake(10, 75)
Brownie = Brownie(25, 25)
Cookie = Cookie(60, 20)
Bun = Bun(30, 60)
Macarons = Macarons(50, 25)

#-------------Access & Update-------------
print("***** Cake *****")
print("Price of cake :: "+str(Cake.Price)+" Baht")
Cake.Price = 125
print("Update cake price :: "+str(Cake.Price)+" Baht", "\n")
print("***** Brownie *****")
print("Price of brownie :: "+str(Brownie.Price)+" Baht")
Cake.Price = 30
print("Update brownie price :: "+str(Brownie.Price)+" Baht", "\n")
 
print("***** Cookie *****")
print("Price of cookie :: "+str(Cookie.Price)+" Baht")
Cake.Price = 125
print("Update cookie price :: "+str(Cookie.Price)+" Baht", "\n")
 
print("***** Bun *****")
print("Price of bun :: "+str(Bun.Price)+" Baht")
Cake.Price = 125
print("Update bun price :: "+str(Bun.Price)+" Baht", "\n")
 
print("***** Macarons *****")
print("Price of macarons :: "+str(Macarons.Price)+" Baht")
Cake.Price = 125
print("Update macarons price :: "+str(Macarons.Price)+" Baht", "\n")
 
print("\n***** Amount of Product *****")
print("Cake amount :: "+str(Cake.Amount)+" Piece")
print("Brownie amount :: "+str(Brownie.Amount)+" Piece")
print("Cookie amount :: "+str(Cookie.Amount)+" Piece")
print("Bun amount :: "+str(Bun.Amount)+" Piece")
print("Marcarons amount :: "+str(Macarons.Amount)+" Piece")
 
Total_amount = Cake.Amount + Brownie.Amount + Cookie.Amount + Bun.Amount + Macarons.Amount
print("Total Amount :: "+str(Total_amount)+" Piece\n")
 
print("*****Employee manager_00 *****")
print("Employee manager_00 name :: "+Employee_Manager.Name)
print("Employee position :: "+Employee_Manager.Position)
 
print("***** Customer 00 *****")
print("Customer_00 name :: "+Customer_00.Name)
print("Customer_00 address :: "+Customer_00.Address)
Customer_00.Address = "Chiang_mai"
print("Update customer_00 address :: "+Customer_00.Address)
