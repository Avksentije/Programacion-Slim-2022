#Creación de una interfaz con Tkinter

#colores: https://www.delftstack.com/es/howto/python/colors-in-python/

from tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        contenedor.title(title)
        self.e1 = Label(contenedor, text = mensaje, fg ='#00FFFF', bg ="black" )
        self.e1.pack()

mensaje = "Hola", "\nSoy una ventana"
title = "thoughts"

ventana = Tk()
miInterfaz = Interfaz (ventana)
ventana.mainloop()  
