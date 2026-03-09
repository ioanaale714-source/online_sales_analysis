from product import Product
class ProductManager:
 def __init__(self):
  self.products=[]
  
 def add_product(self,product) :
  self.products.append(product)
  print(f"Produsul {product.name} a fost adaugat cu succes.")
  
 def dispaly_all_products(self):
     print("\n Lista produse disponibile:")
     if not self.products:
         print("Nu exista produse in lista.")
     else:
         for product in self.products:
             
          product.display_info()
          
 def total_value(self):
     total= sum (p.price * p.quantity for p in self.products)
     print(f"\n Valoarea totala a produselor este de {total} lei.")
     return total
 
manager=ProductManager()
 
prod1=Product("Laptop", 320, 3)
prod2= Product("Phone", 440, 6)
 
manager.add_product(prod1)
manager.add_product(prod2)

manager.dispaly_all_products()
manager.total_value()
 
        
 
 