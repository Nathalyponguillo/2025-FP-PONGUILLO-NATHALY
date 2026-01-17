# Ejemplo de Programación Orientada a Objetos (POO) en Python
# Incluye: Herencia, Encapsulación y Polimorfismo

# Clase Base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."



# Clase Derivada: Estudiante
# Hereda de Persona (ejemplo de herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase padre
        self.carrera = carrera

    # Sobrescribimos el método presentarse (ejemplo de polimorfismo)
    def presentarse(self):
        return f"Soy {self.nombre}, estudiante de {self.carrera}, y tengo {self.edad} años."


# Encapsulación: Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado (encapsulado)

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirado: {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes para el retiro.")

    def obtener_saldo(self):
        # Método getter para acceder al saldo privado
        return self.__saldo



# Polimorfismo con argumentos variables
# Clase Calculadora
class Calculadora:
    def sumar(self, *args):
        # Método que acepta múltiples argumentos (ejemplo de polimorfismo)
        return sum(args)

# DEMOSTRACIÓN DEL PROGRAMA
# Herencia y Polimorfismo
persona1 = Persona("Luis", 40)
estudiante1 = Estudiante("Nathaly", 22, "Tecnología de la Información")

print(persona1.presentarse())      # Usa método de la clase base
print(estudiante1.presentarse())   # Usa método sobrescrito en la clase derivada

# Encapsulación
mi_cuenta = CuentaBancaria(1000)
print(f"Saldo inicial: {mi_cuenta.obtener_saldo()}")
mi_cuenta.depositar(500)
mi_cuenta.retirar(300)
print(f"Saldo final: {mi_cuenta.obtener_saldo()}")

# Polimorfismo con argumentos variables
calc = Calculadora()
print("Suma de 2 números:", calc.sumar(5, 10))
print("Suma de varios números:", calc.sumar(1, 2, 3, 4, 5))