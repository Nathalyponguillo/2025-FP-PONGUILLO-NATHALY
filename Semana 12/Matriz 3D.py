# Definimos las ciudades, días y semanas
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

import random

# Crear matriz 3D: ciudades x días x semanas
# Cada celda contiene una temperatura aleatoria entre 10 y 30 grados
matriz_temperaturas = [[[random.uniform(10, 30) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar promedios semanales por ciudad
for i, ciudad in enumerate(ciudades):
    print(f"\n Promedios semanales para {ciudad}:")
    for semana in range(semanas):
        suma = sum(matriz_temperaturas[i][semana])
        promedio = suma / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f} °C")