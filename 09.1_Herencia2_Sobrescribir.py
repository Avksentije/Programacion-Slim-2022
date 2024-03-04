#DEFINICIÓN DE CLASES: Es el esqueleto del programa principal. 
#El CÓDIGO PRINCIPAL recurrirá a estos cimientos, fundamentados en clases y subclases: 

class Persona: #Clase Persona, constituido por los métodos __init__ y hablar. Usan self para "referenciar"
    def __init__(self, edad, nombre): #Método self (define al objeto "self") constituido de las variables edad y nombre
        self.edad = edad #Atributo .edad guardado en la variable edad
        self.nombre = nombre #Atributo .nombre guardado en la variable nombre
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    def hablar(self, palabras): #Método hablar (refiere al objeto "self", que va a hablar), constituido por la variable palabras
        print (self.nombre, ":", palabras) #.nombre es un atributo del objeto "self"

class Deportista (Persona): #Declaro una nueva clase seguido de (Persona), que es la clase de la cual heredará el método
    def __init__(self, edad, nombre, deporte): #Método self (define al objeto "self") constituido de las variables edad, nombre y deporte
        self.edad = edad #Atributo .edad guardado en la variable edad
        self.nombre = nombre #Atributo .nombre guardado en la variable nombre
        self.deporte = deporte      
        print ("Se ha creado a", self.nombre, "de", self.edad)
        
    def practicarDeporte(self, deporte):
       self.deporte = deporte #cada que declaremos las variables del self, hay que definirlas en el subproceso
       print (self.nombre, ": Voy a practicar", self.deporte)  #es importante definir al self.atributo para que se use el particular
       print (self.nombre, ":¿A ti te gusta", self.deporte, "?")


#CÓDIGO PRINCIPAL: usará las clases ya declaradas y "funcionará" por sí mismo.
#Sólo necesitará que introduzcamos los atributos particulares de cada self = OBJETO
juan = Persona ("17", "Juan") #Atributos particulares del objeto Juan
juan.hablar ("Hola, soy Juan") #Llamada al método hablar y Palabras particulares del objeto Juan

luis = Deportista("18", "Luis", "natación") #Herencia de la clase persona en Deportista y Atributos particulares de Luis
luis.hablar("Hola, ¿qué tal?") #Llamada al método hablar y Palabras particulares del objeto Luis
luis.practicarDeporte(luis.deporte) #Llamado al método practicarDeporte y el atributo deporte particular del objeto

lalo = Deportista("30", "Lalo", "futbol") #Herencia de la clase persona en Deportista y Atributos particulares de Lalo
lalo.hablar("Hola a ambos, yo soy Lalo") #Llamada al método hablar y Palabras particuares del objeto Lalo
lalo.practicarDeporte(lalo.deporte) #Llamada al método practicarDeporte y el atrubuto deporte particular del objeto
