# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    Parámetros:
        base (float): longitud de la base
        altura (float): longitud de la altura
    Retorna:
        float: área del rectángulo
    """
    return base * altura


# Programa principal
def main():
    # Solicitar datos al usuario (string convertido a float)
    base_str = input("Ingrese la base del rectángulo en cm: ")
    altura_str = input("Ingrese la altura del rectángulo en cm: ")

    # Conversión de string a float
    base = float(base_str)
    altura = float(altura_str)

    # Calcular área
    area = calcular_area_rectangulo(base, altura)

    # Uso de boolean para verificar si el área es mayor a 100
    es_grande = area > 100

    # Mostrar resultados
    print(f"\n El área del rectángulo es: {area} cm²")
    print(f"¿El área es mayor a 100 cm²?: {es_grande}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()