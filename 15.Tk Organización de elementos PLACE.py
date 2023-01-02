from tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        contenedor.title(title)
        self.e1 = Label(contenedor, text = mensaje1, fg ='#00FFFF', bg ="black" )
        self.e1.place(x=0, y=0, width=200, height=200) #Definen las coordenadas del elemento en pixeles, x y y la posición respecto al origen; widht y height, el ancho y alto de la caja de la etiqueta  

mensaje1 = "Hola", "\nSoy una ventana", "\nY puedo observarte o.o"
title = "Creepy thoughts"

ventana = Tk()
miInterfaz = Interfaz (ventana)
ventana.mainloop()  