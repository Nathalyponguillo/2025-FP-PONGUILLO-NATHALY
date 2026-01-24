# Ejemplo de Creación de Objetos:
# "Consideremos una clase Computadora con un constructor definido.
# La creación de un objeto Computadora se vería así en Python:"

class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print(f"Computadora {self.marca} {self.modelo} creada.")

mi_pc = Computadora("Lenovo", "ThinkPad X1 Carbon")

# "Aquí, mi_pc es una instancia de la clase Computadora, y se le pasan
# 'Lenovo' y 'ThinkPad X1 Carbon' como argumentos al constructor."


# "Consideremos una clase Conexion que simula la apertura y cierre
# de un recurso externo, como podría ser una base de datos o una red:"
class Conexion:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Conexión '{self.nombre}' inicializada.")

    def __del__(self):
        print(f"Conexión '{self.nombre}' cerrada y liberada.")

# "Aquí, el constructor __init__ se encarga de inicializar el objeto Conexion,
# mientras que el destructor __del__ se encarga de liberarlo."

# Al crear y eliminar instancias de Conexion, se pueden observar las acciones
# de los constructores y destructores:

mi_conexion = Conexion("BaseDeDatosPrincipal")

# La instancia mi_conexion de la clase Conexion es creada y luego eliminada.
# Esto desencadena primero el constructor y luego el destructor, gestionando
# adecuadamente la vida útil del recurso.

del mi_conexion

print("Fin del programa: los destructores se ejecutan automáticamente.")