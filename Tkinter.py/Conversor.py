import tkinter as tk
from tkinter import messagebox
class Conversor():
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.geometry("")
        self.ventana.title("Conversor de temperaturas")
        self.ventana.config(bg="lightgreen")
        tk.Label(self.ventana,text="Temperatura",fg="black").grid(row=0,column=0,padx=50,pady=30,sticky="nsew")
        self.Dato_temp=tk.Entry(self.ventana)
        self.Dato_temp.grid(row=0, column=1)
        tk.Button(self.ventana, text="Convertir a celsius", bg="lightblue", fg="black", command=self.celsius).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.ventana, text="Convertir a fahrenheit", bg="lightblue", fg="black", command=self.fahrenheit).grid(row=1, column=1, padx=10, pady=10,)
        tk.Button(self.ventana, text="limpiar", bg="lightblue", fg="black", command=self.limpiar).grid(row=2, column=0,columnspan=2, padx=50, pady=30,)
        self.resultado = tk.Label(self.ventana, text="El resultado de su conversión, saldrá aquí!!! ", bg="lightgreen",font=("Garamond",13))
        self.resultado.grid(row=3, column=0, columnspan=2, padx=15, pady=10,)
        self.ventana.mainloop()
    def celsius(self):
        try:
            self.fah=float (self.Dato_temp.get())
            self.cel=(self.fah-32) * 5/9
            self.resultado.config(text=f"{self.fah} F = {self.cel:3f} C")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido.")
    def fahrenheit (self):
        try:
            self.cel=float(self.Dato_temp.get())
            self.fah=(self.cel*9/5) +32
            self.resultado.config(text=f"{self.cel} C = {self.fah} F")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido.")
    def limpiar (self):
        self.Dato_temp.delete(0, tk.END)
        self.resultado.config(text="")
    
Conversor()
        