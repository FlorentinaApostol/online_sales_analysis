class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price) 
        self.quantity = int(quantity)
        
     # Metoda afisare informatii
    def display_info(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
     # Metoda actualizare cantitate de produse
    def update_quantity(self, new_quantity):
        self.quantity = int(new_quantity)
        return self.quantity