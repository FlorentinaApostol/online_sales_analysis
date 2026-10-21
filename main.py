from product import Product
from product_manager import ProductManager
from cart import Cart

    

if __name__ == "__main__":
    manager = ProductManager() # Creare instanta ProductManager

    products = [
        Product("Laptop Gaming", 4200.0, 4),
        Product("Mouse", 150.0, 20),
        Product("Tastatura wireless", 250.0, 15),
        Product("Casti", 225.0, 10),
        Product("Boxe", 550.0, 3)
    ]
# Adaugare produse
for p in products:
    manager.add_product(p)

# Afisarea produselor si valoarea totala a inventarului

manager.display_all_products()
print (f"Valoarea totala: {manager.calculate_total_value()} Ron")
manager.remove_product("Mouse")

 # Creare instanta Cart

cart = Cart()
cart.add_to_cart(products[0], quantity = 1)
cart.add_to_cart(products[3], quantity = 2)

cart.display_cart()
print(f"Valoarea totala de plata: {cart.calculate_total_cart()} RON")
