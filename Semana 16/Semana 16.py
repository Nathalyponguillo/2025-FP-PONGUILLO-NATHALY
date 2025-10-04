# Escritura de archivo
with open("my_notes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hoy aprendí a manejar archivos en Python.\n")
    archivo.write("Me gusta cómo se puede automatizar la escritura y lectura.\n")
    archivo.write("Este conocimiento será útil para proyectos futuros.\n")

# Lectura línea por línea
with (open("my_notes.txt", "r", encoding="utf-8") as archivo):
    for linea in archivo:
        print(linea.strip())  # Elimina el salto de línea al final

    # Cerramos el archivo de lectura
    archivo.close()
