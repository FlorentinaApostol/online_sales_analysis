from product import Product
class ProductManager:
    def __init__(self):
        self.products = []

     # Metoda adaugare produse
    def add_product(self, product):
        self.products.append(product)
    
     # Metoda de afisare a tuturor produselor
    def display_all_products(self):
        for product in self.products:
            print(product.display_info())

      # Metoda calcul valoare totala produse
    def calculate_total_value(self):
        return sum(product.price* product.quantity for product in self. products)

      # Metoda eliminare produse dupa nume
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print (f"Produsul {product_name} a fost sters cu succes!")
                return
        print(f"Produsul {product_name} nu a fost gasit!")



