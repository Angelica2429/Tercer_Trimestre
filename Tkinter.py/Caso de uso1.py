import tkinter as tk
from tkinter import messagebox 
class Productos():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Productos")
        self.ventana.geometry("400x300")
        self.ventana.config(bg="Lightblue")
        
        self.productos ={
                "leche":"Precio = 3000,Cantidad = 40",
                "harina":"Precio = 5400,Cantidad = 90",
                "huevos":"Precio = 900,Cantidad = 45",
                "polvo_hornear":"Precio = 2000,Cantidad = 89"
                }
        tk.Button(self.ventana, text="Mostrar productos",bg="white",fg="black",command=self.mostrar_productos).grid(row=0,column=1,padx=20,pady=10)
        self.ventana.mainloop()
        
    def mostrar_productos(self):
        self.mensaje = (
             "leche: Precio = 3000, Cantidad = 40\n"
             "harina: Precio = 5400, Cantidad = 90\n"
             "huevos: Precio = 900, Cantidad = 45\n"
             "polvo de hornear: Precio = 2000, Cantidad = 89"
)
        messagebox.showinfo("Lista de productos", self.mensaje)

Productos()



