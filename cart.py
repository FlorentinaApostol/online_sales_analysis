class Cart:
    def __init__(self):
        self.cart_items = []

# Metoda de adaugare produse in cos
    def add_to_cart(self, product, quantity = 1):
        self.cart_items.append({'product': product, 'quantity': quantity})

# Metoda calcul valoare totala a cosului
    def calculate_total_cart(self):
        total = 0
        for cart_item in self.cart_items:
            p = cart_item['product']
            qty = cart_item['quantity']
            total += p.price * qty
        return total

# Metoda de afisare a cosului
    def display_cart(self):
        print("--- Continutul cosului de cumparaturi ---")
        if not self.cart_items:
            print("Cosul este gol.")
        for cart_item in self.cart_items:
             p = cart_item['product']
             qty = cart_item['quantity']
             print(f"Produs: {p.name}, Pret unitar: {p.price} RON, Cantitate: {qty}")

         
        
