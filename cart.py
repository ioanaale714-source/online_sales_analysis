class Cart:

 def __init__(self):
    self.cart_items=[]
        
 def add_to_cart(self, product):
    self.cart_items.append(product)
    print(f"Produsul {product.name} a fost adaugat in cos.")
   
 def calculate_total(self):
    total=sum(p.price*p.quantity for p in self.cart_items)
    return total
  
 def display_cart(self):
    print("\n Continut cos de cumparaturi:" )
    if not self.cart_items:     
            print("Cosul este gol.")
    else:
        for p in self.cart_items:
            p.display_info()
        print(f"Total de plata: {self.calculate_total()} lei.")
  
       
        