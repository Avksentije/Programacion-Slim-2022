

from tkinter import *

class Interfaz:
    def __init__(self, contenedor):
        contenedor.title(title)
        self.e1 = Label(contenedor, text = mensaje1, fg ='#00FFFF', bg ="black" )
        self.e2 = Label(contenedor, text = mensaje2, fg="lime", bg="plum")
        self.e3 = Label(contenedor, text = mensaje3, fg="yellow", bg="black")
        self.e4 = Label(contenedor, text = mensaje4, fg ='#00FFFF', bg ="black" )
        self.e5 = Label(contenedor, text = mensaje5, fg="lime", bg="plum")
        self.e6 = Label(contenedor, text = mensaje6, fg="yellow", bg="black")

        self.e1.grid(column=0, row=0)  
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=1, row=0)  
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)

mensaje1 = "Hola", "\nSoy una ventana", "\nY puedo observarte o.o"
mensaje2 = "Caleidoscopios de cascabel"
mensaje3 = "Cric-trec-crac"
mensaje4 = "Hola", "\nSoy una ventana", "\nY puedo observarte o.o"
mensaje5 = "Caleidoscopios de cascabel"
mensaje6 = "Cric-trec-crac"

title = "Creepy thoughts"

ventana = Tk()
miInterfaz = Interfaz (ventana)
ventana.mainloop()  