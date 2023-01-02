class Persona:
    def __init__(self): #método 1 : define los atributos del objeto persona (Juan, 18)
        self.edad = 18
        self.nombre = "Juan"
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    def hablar(self, palabras = "No sé qué decir"): #método para que Juan "hable"
        print (self.nombre, ":", palabras)

juan = Persona()                       #Clase persona definida en la variable juan y método "self"
juan.hablar()
juan.hablar("Hola, estoy hablando")    #En este caso, la línea 12 sobrescribe la línea 7