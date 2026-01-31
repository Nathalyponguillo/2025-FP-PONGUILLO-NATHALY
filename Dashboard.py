import os
import subprocess
from colorama import Fore, Style

def mostrar_codigo(ruta_script):
    """
    Muestra el contenido de un script en consola.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(Fore.CYAN + f"\n--- Código de {ruta_script} ---\n" + Style.RESET_ALL)
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(Fore.RED + "El archivo no se encontró." + Style.RESET_ALL)
        return None
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al leer el archivo: {e}" + Style.RESET_ALL)
        return None

def ejecutar_codigo(ruta_script):
    """
    Ejecuta un script en una nueva ventana de terminal.
    Compatible con Windows y sistemas Unix.
    """
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error al ejecutar el código: {e}" + Style.RESET_ALL)

def registrar_historial(ruta_script):
    """
    Registra en un archivo historial.txt los scripts ejecutados.
    """
    with open("historial.txt", "a") as log:
        log.write(f"Ejecutado: {ruta_script}\n")

def mostrar_menu():
    """
    Muestra el menú principal con las unidades detectadas automáticamente.
    """
    ruta_base = os.path.dirname(__file__)
    # Detecta automáticamente las carpetas de unidades
    unidades = {str(i+1): f.name for i, f in enumerate(os.scandir(ruta_base)) if f.is_dir()}

    while True:
        print(Fore.GREEN + "\nMenu Principal - Dashboard" + Style.RESET_ALL)
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print(Fore.YELLOW + "Saliendo del programa." + Style.RESET_ALL)
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo." + Style.RESET_ALL)

def mostrar_sub_menu(ruta_unidad):
    """
    Muestra las subcarpetas dentro de una unidad.
    """
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(Fore.BLUE + "\nSubmenú - Selecciona una subcarpeta" + Style.RESET_ALL)
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo." + Style.RESET_ALL)

def mostrar_scripts(ruta_sub_carpeta):
    """
    Lista los scripts .py en una subcarpeta y permite verlos o ejecutarlos.
    """
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(Fore.MAGENTA + "\nScripts - Selecciona un script para ver y ejecutar" + Style.RESET_ALL)
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                            registrar_historial(ruta_script)
                        elif ejecutar == '0':
                            print(Fore.YELLOW + "No se ejecutó el script." + Style.RESET_ALL)
                        else:
                            print(Fore.RED + "Opción no válida. Regresando al menú de scripts." + Style.RESET_ALL)
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Opción no válida. Por favor, intenta de nuevo." + Style.RESET_ALL)

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()