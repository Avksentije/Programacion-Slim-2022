class Persona:
    def __init__(self): #método 1 : define los atributos del objeto persona (Juan, 18)
        self.edad = 18
        self.nombre = "Juan"
        print ("Se ha creado a", self.nombre, "de", self.edad, "años")
    
    def hablar(self, palabras): #método para que Juan "hable"
        print (self.nombre, ":", palabras)

juan = Persona()                       #Clase persona definida en la variable juan y método "self"
juan.hablar("Hola, estoy hablando")    #Continúa la clase persona, definida antes como la variable juan, con el método .hablar