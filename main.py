from product import Product
from product_manager import ProductManager

# Creare instanta ProductManager
    

if __name__ == "__main__":
    manager = ProductManager()

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

