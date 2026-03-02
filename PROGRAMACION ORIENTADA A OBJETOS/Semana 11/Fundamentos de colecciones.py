import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if p.get_nombre().lower() == nombre.lower()]
        return resultados

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, archivo)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = {int(id): Producto(**info) for id, info in datos.items()}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado, iniciando inventario vacío.")


def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("ID: "))
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontró el producto.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()