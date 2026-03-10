from product import Product
from product_manager import ProductManager
from cart import Cart
def main():
    manager=ProductManager()
    cos=Cart()
    
    p1=Product("Mouse", 3500, 4)
    p2=Product("Monitor", 2670, 1)
    p3=Product("Phone", 220, 8)
    
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