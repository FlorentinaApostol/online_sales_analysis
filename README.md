# Online Sales Analysis

Proiect dezvoltat în Python pentru gestionarea și analizarea produselor, a stocurilor și a coșului de cumpărături într-un magazin online, versionat utilizând Git.

 Descrierea Claselor și Funcționalităților
 1. Clasa Product (product.py)
Modelul de bază pentru fiecare articol din magazin.
 Atribute: name (nume produs), price (preț unitar), quantity (cantitate în stoc).
 Rol: Menține datele despre un produs individual.

 2. Clasa ProductManager (product_manager.py)
Modulul de administrare a inventarului general.
 Atribute: products (listă de produse).
 Metode și Funcționalități:
  * add_product(product): Adaugă un produs nou în inventar.
  * remove_product(name): Elimină un produs din stoc după nume.
  * display_all_products(): Afișează toate produsele disponibile în consolă.
  * calculate_total_value(): Calculează valoarea totală a tuturor produselor din stoc.

 3. Clasa Cart (cart.py)
Modulul care gestionează coșul de cumpărături al unui client.
 Atribute: cart_items (listă cu produsele adăugate și cantitatea lor).
 Metode și Funcționalități:
  * add_to_cart(product, quantity): Adaugă un număr specificat de bucăți dintr-un produs în coș.
  * display_cart(): Afișează conținutul curent al coșului de cumpărături.
  * calculate_total_cart(): Calculează și returnează suma totală de plată pentru articolele din coș.


 Execuția Proiectului (main.py)
Fișierul principal integrează toate modulele:
1. Creează o instanță ProductManager.
2. Afișează valoarea totală a inventarului și permite eliminarea de produse.
3. Creează un coș de cumpărături (Cart), adaugă produse în el și afișează totalul de plată.