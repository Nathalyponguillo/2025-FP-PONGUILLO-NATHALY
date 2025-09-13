
promedios_semanales = {
    "Quito": [22.5, 23.1, 24.0, 22.8],
    "Guayaquil": [27.2, 28.0, 27.5, 28.3],
    "Cuenca": [19.8, 20.1, 19.5, 20.0]
}
def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}
    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = round(promedio, 2)
    return temperaturas_promedio

# Calcular y mostrar resultados
resultados = temperatura_promedio(promedios_semanales)

print("🌡️ Promedio total por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio} °C")