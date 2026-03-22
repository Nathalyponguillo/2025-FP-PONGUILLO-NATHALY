import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # Necesario para el DatePicker

# ---------------------------
# Clase principal de la Agenda
# ---------------------------
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame principal para organizar la interfaz
        frame_lista = tk.Frame(root)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        frame_formulario = tk.Frame(root)
        frame_formulario.pack(fill="x", padx=10, pady=5)

        frame_botones = tk.Frame(root)
        frame_botones.pack(fill="x", padx=10, pady=5)

        # ---------------------------
        # TreeView para mostrar eventos
        # ---------------------------
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill="both", expand=True)

        # ---------------------------
        # Campos de entrada
        # ---------------------------
        tk.Label(frame_formulario, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_formulario, width=12, background="darkblue", foreground="white", borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_formulario, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_formulario)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_formulario, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_formulario, width=40)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # ---------------------------
        # Botones de acción
        # ---------------------------
        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side="left", padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right", padx=5)

    # ---------------------------
    # Funciones de manejo de eventos
    # ---------------------------
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        desc = self.desc_entry.get()

        if fecha and hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar el evento seleccionado?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Selección vacía", "No hay evento seleccionado para eliminar.")

# ---------------------------
# Ejecución de la aplicación
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()