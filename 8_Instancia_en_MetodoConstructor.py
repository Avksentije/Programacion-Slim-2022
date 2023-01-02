#Se define la clase Persona, la cual tendrá objetos (instancias o self)
#Cada instancia puede tener .atributos, alojados en el valor o función que le asignemos (ej. self.edad = edad o self.edad = "25")

class Persona:
    def __init__(self, edad, nombre): #directamente la clase Persona se construye con el método self que toma edad, nombre de los objetos que vayamos declarando (Juan y Luis)
        self.edad = edad
        self.nombre = nombre
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    def hablar(self, palabras): #método para que la Persona "hable"
        print (self.nombre, ":", palabras)

juan = Persona("22", "Juan")  #juan es un objeto con los atributos contenidos en la clase Persona (EDAD Y NOMBRE)                     
juan.hablar("Hola, soy Juan y estoy hablando") #juan puede hablar porque definimos el método hablar orientado a self (que es el objeto o instancia)    
luis = Persona("18", "Luis")  #creamos a luis, con su edad y nombre específicos.                 
luis.hablar("Hola, soy Luis y estoy hablando")  #creamos lo que luis hablará
