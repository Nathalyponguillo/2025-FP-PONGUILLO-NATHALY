import tkinter as tk
from tkinter import messagebox

# --- Funciones principales ---
def agregar_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes añadir una tarea vacía.")

def completar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        indice = seleccion[0]
        tarea = lista_tareas.get(indice)
        # Añadir prefijo ✔ para marcar completada
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
    else:
        messagebox.showinfo("Info", "Selecciona una tarea para marcarla como completada.")

def eliminar_tarea(event=None):
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion[0])
    else:
        messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

def cerrar_app(event=None):
    ventana.quit()

# --- Interfaz gráfica ---
ventana = tk.Tk()
ventana.title("Gestión de Tareas")
ventana.geometry("400x300")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Añadir", command=agregar_tarea)
btn_agregar.grid(row=0, column=0, padx=5)

btn_completar = tk.Button(frame_botones, text="Completar", command=completar_tarea)
btn_completar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_tarea)
btn_eliminar.grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# --- Atajos de teclado ---
ventana.bind("<Return>", agregar_tarea)       # Enter para añadir
ventana.bind("<c>", completar_tarea)          # C para completar
ventana.bind("<d>", eliminar_tarea)           # D para eliminar
ventana.bind("<Delete>", eliminar_tarea)      # Tecla Delete para eliminar
ventana.bind("<Escape>", cerrar_app)          # Escape para cerrar

ventana.mainloop()
