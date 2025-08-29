# Búsqueda en Arreglo Multidimensional

# Definir la matriz 3x3
matriz = [
    [10, 25, 30],
    [5, 18, 22],
    [7, 14, 60]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición
    return None

# Valor a buscar
valor_buscado = 22

# Ejecución de la búsqueda
posicion = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if posicion:
    print(f"\ntrue El valor {valor_buscado} se encontró en la posición {posicion}")
else:
    print(f"\nfalse El valor {valor_buscado} no se encontró en la matriz")

