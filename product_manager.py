from product import Product
class ProductManager:
 def __init__(self):
  self.products=[]
  
 def add_product(self,product) :
  self.products.append(product)
  print(f"Produsul {product.name} a fost adaugat cu succes.")
  
 def display_all_products(self):
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
 

 def remove_product(self, name):
    initial_count= len(self.products)
    self.products=[p for p in self.products if p.name != name]
    if len(self.products)<initial_count:
        print(f"Produsul {name} a fost eliminat.")
    else:
        print(f"Produsul {name} nu a fost gasit.")
 
        
 
 