import tkinter as tk
from tkinter import messagebox

class Lista_tareas():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("lista de tareas")
        self.ventana.geometry("500x300")
        self.ventana.config(bg="#c999af")
        self.entrada_tarea = tk.Entry(self.ventana, width=40)
        self.entrada_tarea.pack(pady=10)
        self.lista_tareas = tk.Listbox(self.ventana, width=50, height=10)
        self.lista_tareas.pack(pady=10)
        
        tk.Button(self.ventana,text="Agregar tarea", bg="white",fg="black",command=self.agregar_tareas).pack(pady=5)
        tk.Button(self.ventana, text="Eliminar tarea", bg ="red",fg="white",command=self.eliminar_tarea).pack(pady=5)
        self.ventana.mainloop()
    def agregar_tareas(self):
        self.tarea=self.entrada_tarea.get()
        if self.entrada_tarea!="":
            self.lista_tareas.insert(tk.END, self.tarea)
            self.entrada_tarea.delete(0,tk.END)
        else:
            messagebox.showwarning("Escribe una tarea antes de agregarla, graciaaas")
    def eliminar_tarea(self):
        try:
            self.seleccion = self.lista_tareas.curselection()
            self.lista_tareas.delete(self.seleccion)
        except:
            messagebox.showwarning("Seleccione la tarea antes de eliminarla,graciaaas")
Lista_tareas()