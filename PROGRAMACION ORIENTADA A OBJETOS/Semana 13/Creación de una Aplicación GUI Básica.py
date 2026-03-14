import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos Básico")
ventana.geometry("400x300")

# Etiqueta
label = tk.Label(ventana, text="Ingrese información:")
label.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Funciones de los botones
def agregar_dato():
    dato = entrada.get()
    if dato.strip():  # Evita agregar texto vacío
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un texto válido.")

def limpiar_lista():
    lista.delete(0, tk.END)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()