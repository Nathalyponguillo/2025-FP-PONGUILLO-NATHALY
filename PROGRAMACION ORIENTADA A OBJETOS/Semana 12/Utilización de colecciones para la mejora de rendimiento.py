# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para título y autor
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN -> Libro
        self.usuarios = set()  # Conjunto de IDs únicos
        self.registro_usuarios = {}  # ID -> Usuario

    # Añadir libro
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("El libro no existe en la biblioteca.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.registro_usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya existe.")

    # Dar de baja usuario
    def baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            eliminado = self.registro_usuarios.pop(id_usuario)
            print(f"Usuario dado de baja: {eliminado}")
        else:
            print("El usuario no está registrado.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.registro_usuarios[id_usuario]
            libro = self.libros.pop(isbn)
            usuario.libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {usuario.nombre}")
        else:
            print("Usuario o libro no disponible.")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f" Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    # Buscar libros
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    # Listar libros prestados
    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.registro_usuarios[id_usuario]
            return usuario.libros_prestados
        else:
            print("Usuario no registrado.")
            return []


# Bloque de demostración para ejecutar y verificar comportamiento
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Crear algunos libros y agregarlos
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-3-16-148410-0")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "978-0-06-112241-5")
    libro3 = Libro("Programación en Python", "Autor Ejemplo", "Educación", "111-1-11-111111-1")

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Ana", "U001")
    usuario2 = Usuario("Luis", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    print("\n--- Prestamos y devoluciones ---")
    biblioteca.prestar_libro("U001", "978-3-16-148410-0")  # Ana toma Cien Años de Soledad
    biblioteca.prestar_libro("U001", "000-0")  # ISBN inexistente

    print("\nLibros prestados a Ana:", biblioteca.listar_libros_prestados("U001"))

    biblioteca.devolver_libro("U001", "978-3-16-148410-0")
    print("\nBuscar por autor 'Antoine':", biblioteca.buscar_libros("autor", "Antoine"))

    biblioteca.quitar_libro("978-0-06-112241-5")

    biblioteca.baja_usuario("U002")
