#Organizadores de contenido
#pack - los ordena uno tras otro
#grid - distribuye los elementos en filas y columnas
#place - posiciona los elementos en coordenadas en específico

#PACK - odena los elementos conforme estos llamen al método
#Puede colocarse hacia las orillas o llenar el largo y ancho restante de su contenedor (posición del cuadrante)

from tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        contenedor.title(title)
        self.e1 = Label(contenedor, text = mensaje1, fg ='#00FFFF', bg ="black" )
        self.e2 = Label(contenedor, text = mensaje2, fg="lime", bg="plum")
        self.e3 = Label(contenedor, text = mensaje3, fg="yellow", bg="black")

        self.e1.pack(side = TOP) #Coloca arriba 
        self.e2.pack(side = RIGHT)
        self.e3.pack(side = BOTTOM, fill = BOTH)

mensaje1 = "Hola", "\nSoy una ventana", "\nY puedes observar a través de mi"
mensaje2 = "Caleidoscopios de cascabel"
mensaje3 = "Cric-trec-crac"
title = "Soul-ty thoughts"

ventana = Tk()
miInterfaz = Interfaz (ventana)
ventana.mainloop()  
