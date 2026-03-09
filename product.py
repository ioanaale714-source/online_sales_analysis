class Product:

 def __init__(self, name ,price, quantity):
     self.name=name
     self.price=price
     self.quantity= quantity 
     
 def display_info(self):  
    print(f"Produs: {self.name}. ") 
    print(f"Pret: {self.price} lei.")
    print(f"Cantitate: {self.quantity}.")
    
 def update_quantity(self, new_quantity):
    self.quantity= new_quantity
    print(f"Stoc actualizat pentru {self.name}: {self.quantity} unitati.")
    
produs_test=Product("Laptop", 250, 2)
produs_test.display_info()
produs_test.update_quantity(5)
