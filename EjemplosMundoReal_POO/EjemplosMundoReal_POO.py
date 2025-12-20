# Producto
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int = 1):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (stock: {self.stock})"

    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, precio={self.precio:.2f}, stock={self.stock})"# Carrito
        class Carrito:
    def __init__(self):
                # lista de tuplas: (producto, cantidad)
                self.productos = []

    def agregar_producto(self, producto: Producto, cantidad: int = 1):
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor que 0.")
                if hasattr(producto, "stock") and producto.stock < cantidad:
                    return False, f"Stock insuficiente para {producto.nombre}."

                # reducir stock si aplica
                if hasattr(producto, "stock"):
                    producto.stock -= cantidad

                # actualizar si ya existe en el carrito
                for i, (p, c) in enumerate(self.productos):
                    if p.nombre == producto.nombre:
                        self.productos[i] = (p, c + cantidad)
                        return True, f"Se agregaron {cantidad} x {producto.nombre}."

                self.productos.append((producto, cantidad))
                return True, f"Se agregaron {cantidad} x {producto.nombre}."

            def mostrar_carrito(self) -> str:
                if not self.productos:
                    return "🛒 Carrito vacío."
                lines = ["🛒 Carrito de compras:"]
                for p, c in self.productos:
                    lines.append(f"- {p.nombre} x{c} = ${p.precio * c:.2f}")
                lines.append(f"Total: ${self.calcular_total():.2f}")
                return "\n".join(lines)

            def calcular_total(self) -> float:
                return sum(p.precio * c for p, c in self.productos)

            def vaciar(self):
                self.productos.clear()# Inventario
                class Inventario:
                    def __init__(self, productos=None):
                        self.productos = list(productos) if productos else []

                    def listar(self):
                        return self.productos

                    def agregar(self, producto: Producto):
                        self.productos.append(producto)

                    def buscar_por_indice(self, indice: int):
                        if 0 <= indice < len(self.productos):
                            return self.productos[indice]
                        return None# InterfazCLI
                        import os
                        import time

                        class InterfazCLI:
                            def __init__(self, inventario: Inventario, carrito: Carrito):
                                self.inventario = inventario
                                self.carrito = carrito

                            def clear(self):
                                os.system("cls")

                            def mostrar_menu(self):
                                print("=== Tienda Virtual ===")
                                print("1. Ver catálogo")
                                print("2. Añadir al carrito")
                                print("3. Ver carrito")
                                print("4. Pagar")
                                print("5. Salir")

                            def ejecutar(self):
                                while True:
                                    self.clear()
                                    self.mostrar_menu()
                                    opc = input("Seleccione una opción: ").strip()
                                    if opc == "1":
                                        self.clear()
                                        print("Catálogo:")
                                        for i, p in enumerate(self.inventario.listar()):
                                            print(f"{i}. {p}")
                                        input("\nPresione Enter para volver...")
                                    elif opc == "2":
                                        self.clear()
                                        for i, p in enumerate(self.inventario.listar()):
                                            print(f"{i}. {p}")
                                        idx = input("Índice del producto: ").strip()
                                        if not idx.isdigit():
                                            input("Índice inválido. Enter para continuar.")
                                            continue
                                        producto = self.inventario.buscar_por_indice(int(idx))
                                        if not producto:
                                            input("Producto no encontrado. Enter para continuar.")
                                            continue
                                        cantidad = input("Cantidad: ").strip()
                                        if not cantidad.isdigit() or int(cantidad) <= 0:
                                            input("Cantidad inválida. Enter para continuar.")
                                            continue
                                        ok, msg = self.carrito.agregar_producto(producto, int(cantidad))
                                        input(msg + "\nEnter para continuar.")
                                    elif opc == "3":
                                        self.clear()
                                        print(self.carrito.mostrar_carrito())
                                        input("\nPresione Enter para volver...")
                                    elif opc == "4":
                                        self.clear()
                                        print(self.carrito.mostrar_carrito())
                                        total = self.carrito.calcular_total()
                                        if total == 0:
                                            input("Carrito vacío. Enter para continuar.")
                                            continue
                                        confirmar = input(f"Pagar ${total:.2f}? (s/n): ").strip().lower()
                                        if confirmar == "s":
                                            print("Procesando pago...")
                                            time.sleep(1)
                                            self.carrito.vaciar()
                                            input("Pago completado. Gracias. Enter para continuar.")
                                        else:
                                            input("Pago cancelado. Enter para continuar.")
                                    elif opc == "5":
                                        break
                                    else:
                                        input("Opción inválida. Enter para continuar.")
