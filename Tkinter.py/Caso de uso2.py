import tkinter as tk
class Presupuesto():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Presupuesto")
        self.ventana.geometry("500x300")
        self.ventana.config(bg="lightblue")
        tk.Label(self.ventana,text="Decoración").place(relx=0.05,rely=0.05,relwidth=0.20,height=0.20)
        self.ventana.decoracion=tk.Entry(self.ventana)
        self.ventana.decoracion.pack()
        self.ventana.mainloop()

Presupuesto()

