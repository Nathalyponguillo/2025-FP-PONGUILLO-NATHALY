# Programación Tradicional en Python
# Ejemplo: Registro de temperaturas semanales

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # 7 días de la semana
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    print("Registro de temperaturas semanales")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")

# Ejecutar
if __name__ == "__main__":
    main()
# Programación Orientada a Objetos (POO) en Python
# Ejemplo: Registro de temperaturas semanales

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []  # Encapsulamos la lista de temperaturas

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Herencia: una clase que extiende ClimaDiario para mostrar resultados
class ClimaSemanal(ClimaDiario):
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C")
# Programa principal
def main():
    print("Registro de temperaturas semanales (POO)")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

# Ejecutar
if __name__ == "__main__":
    main()