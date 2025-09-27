#informacion_personal
print("Informacion Personal")
persona = {"nombre": "Luciana", "edad": 20, "ciudad": "Quito"}
print("Diccionario original:", persona)

# Insertar
persona["profesion"] = "Ingeniera"
print("Después de insertar 'profesion':", persona)

# Eliminar un elemento
del persona["edad"]
print("Después de eliminar 'edad':", persona)

# Borrar todo el diccionario
persona.clear()
print("Después de limpiar el diccionario:", persona)