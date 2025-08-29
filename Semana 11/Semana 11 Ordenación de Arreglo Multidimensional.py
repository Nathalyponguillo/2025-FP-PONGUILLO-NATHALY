# Ordenación de Arreglo Multidimensional

# Definir la matriz 3x3
matriz = [
    [12, 5, 9],
    [8, 3, 15],
    [7, 20, 2]
]

# Función para ordenar una fila con Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n-1):
        for j in range(n-1-i):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar fila a ordenar (ejemplo: fila 1 → segunda fila)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar matriz modificada
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)
