from tkinter import *
ventana = Tk()
ventana.geometry("400x300")
ventana.title("Formulario")
ventana.configure(bg ="lightblue")
ventana.option_add("*Font", "Georgia 36")
titulo=Label(ventana,text="Formulario",bg="lightblue",anchor="n")
titulo.pack()
ventana.mainloop()



