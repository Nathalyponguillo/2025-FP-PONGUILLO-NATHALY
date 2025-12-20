class Product:
    """Representa un producto en la tienda."""

    def __init__(self, name, price, stock):
        """Inicializa un nuevo producto con nombre, precio y stock disponible."""
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        """Reduce el stock del producto si hay suficiente cantidad."""
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def __str__(self):
        """Devuelve una representación en cadena del producto."""
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class Customer:
    """Representa un cliente de la tienda."""

    def __init__(self, name):
        """Inicializa un cliente con su nombre y carrito vacío."""
        self.name = name
        self.cart = []

    def add_to_cart(self, product, quantity):
        """Agrega un producto al carrito si hay stock disponible."""
        if product.reduce_stock(quantity):
            self.cart.append((product, quantity))
            print(f"{self.name} agregó {quantity} unidad(es) de {product.name} al carrito.")
        else:
            print(f"No hay suficiente stock de {product.name}.")

    def checkout(self):
        """Finaliza la compra mostrando el total."""
        total = sum(product.price * quantity for product, quantity in self.cart)
        print(f"🛍️ {self.name} ha realizado la compra. Total: ${total}")
        self.cart.clear()


class Store:
    """Representa la tienda que contiene productos."""

    def __init__(self, name):
        """Inicializa la tienda con un nombre y lista de productos."""
        self.name = name
        self.products = []

    def add_product(self, product):
        """Agrega un producto al catálogo de la tienda."""
        self.products.append(product)
        print(f"📦 Producto agregado: {product.name}")

    def show_products(self):
        """Muestra todos los productos disponibles en la tienda."""
        print(f"Catálogo de la tienda {self.name}:")
        for product in self.products:
            print(f"- {product}")


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Store("TechShop")

    producto1 = Product("Laptop", 800, 5)
    producto2 = Product("Mouse", 25, 10)

    tienda.add_product(producto1)
    tienda.add_product(producto2)

    tienda.show_products()

    cliente = Customer("Ana")
    cliente.add_to_cart(producto1, 1)
    cliente.add_to_cart(producto2, 2)

    cliente.checkout()
    tienda.show_products()
