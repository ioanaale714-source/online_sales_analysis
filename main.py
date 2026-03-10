from product import Product
from product_manager import ProductManager
from cart import Cart
def main():
    manager=ProductManager()
    cos=Cart()
    
    p1=Product("Laptop", 3500, 4)
    p2=Product("Phone", 2670, 2)
    p3=Product("Monitor", 120, 8)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    
    print("\n Testare cos...")
    cos.add_to_cart(p1)
    cos.add_to_cart(p3)
    cos.add_to_cart(p2)
    cos.display_cart()
if __name__=="__main__":
 main()