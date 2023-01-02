

from tkinter import *

class Interfaz: 
    def __init__(self, contenedor): #in this case, def is a method because it is associated to a class
        self.textoE3=StringVar()
         
        contenedor.title(title)
        self.e1 = Label(contenedor, text = mensaje1, fg ='#00FFFF', bg ="black" )
        self.e2 = Label(contenedor, text = mensaje2, fg="lime", bg="plum")
        self.e3 = Label(contenedor, text = mensaje3, fg="yellow", bg="black")
        self.e4 = Button(contenedor, text = mensaje4, fg ='#00FFFF', bg ="black", command=self.hacerConversion)
        self.e5 = Entry(contenedor, fg="lime", bg="plum")
        self.e6 = Label(contenedor, text = "", fg="yellow", bg="black", textvariable=self.textoE3)


        self.e1.grid(column=0, row=0, columnspan=2)  
        self.e2.grid(column=0, row=1)
        self.e3.grid(column=0, row=2)
        self.e4.grid(column=0, row=3, columnspan=2)  
        self.e5.grid(column=1, row=1)
        self.e6.grid(column=1, row=2)

    def hacerConversion(self):
        cel = float(self.e5.get())
        far = (cel * 1.8) + 32
        self.textoE3.set(far)

mensaje1 = "Convertir Celsius a Farenheit"
mensaje2 = "Celsius"
mensaje3 = "Farenheit"
mensaje4 = "Convertir ahora"
mensaje5 = "Caleidoscopios de cascabel"
#mensaje6 = "Cric-trec-crac"

title = "Creepy thoughts"

ventana = Tk()
miInterfaz = Interfaz (ventana)
ventana.mainloop()