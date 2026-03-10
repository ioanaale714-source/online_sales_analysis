from product import Product
from product_manager import ProductManager
def main():
    manager=ProductManager()
    
    p1=Product("Laptop", 3500, 4)
    p2=Product("Phone", 2670, 2)
    p3=Product("Monitor", 120, 8)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    
    manager.display_all_products()
    manager.total_value()
    
if __name__=="__main__":
  main()
    