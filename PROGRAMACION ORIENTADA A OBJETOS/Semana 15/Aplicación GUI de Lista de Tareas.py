import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Enter añade tarea

        # Botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        btn_add = tk.Button(frame_buttons, text="Añadir Tarea", command=self.add_task)
        btn_add.grid(row=0, column=0, padx=5)

        btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", command=self.complete_task)
        btn_complete.grid(row=0, column=1, padx=5)

        btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.complete_task)  # Doble clic marca completada

        # Diccionario para estados de tareas
        self.tasks = {}

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.tasks[task] = False  # False = no completada
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de añadirla.")

    def complete_task(self, event=None):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if not self.tasks[task]:
                self.tasks[task] = True
                # Actualizar visualmente
                self.listbox.delete(index)
                self.listbox.insert(index, f"[✔] {task}")
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index).replace("[✔] ", "")
            self.listbox.delete(index)
            del self.tasks[task]
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
