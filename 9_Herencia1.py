class Persona: #Clase Persona, constituido por los métodos __init__ y hablar. Usan self para "referenciar"
    def __init__(self, edad, nombre): #Método self (define al objeto "self") constituido de las variables edad y nombre
        self.edad = edad #Atributo .edad guardado en la variable edad
        self.nombre = nombre #Atributo .nombre guardado en la variable nombre
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    def hablar(self, palabras): #Método hablar (refiere al objeto "self", que va a hablar), constituido por la variable palabras
        print (self.nombre, ":", palabras) #.nombre es un atributo del objeto "self"

class Deportista (Persona): #Declaro una nueva clase seguido de (Persona), que es la clase de la cual heredará el método

    def practicarDeporte(self, deporte):
        self.deporte = deporte
        print(self.nombre, ": Voy a practicar", self.deporte, "¿A ti te gusta la", self.deporte, "?")  


juan = Persona ("17", "Juan")
juan.hablar ("Hola, soy Juan") #Hace referencia a las palabras del objeto Juan

luis = Deportista("18", "Luis")
luis.hablar("Hola, estoy hablando. ¡Este otro también soy yo!") #Palabras del objeto Luis
luis.practicarDeporte("natación") #Hace referencia al deporte del objeto Luis

lalo = Deportista("30", "Lalo")
lalo.hablar("Hola a ambos, yo soy Lalo") #Palabras del objeto Lalo
lalo.practicarDeporte("futbol") #Hace referencia al deporte del objeto Lalo
