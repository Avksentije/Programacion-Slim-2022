#CLASE ABSTRACTA

from abc import ABC, ABCMeta, abstractmethod 
class Persona:
    __metaclass__=ABCMeta #Esto indica al programa que la clase persona es abstracta. Son dos guiones bajos al inicio y al final de la metaclass.

    def __init__(self, edad, nombre): 
        self.edad = edad
        self.nombre = nombre 
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    @abstractmethod   #Esto indica al programa que es un método abstracto.
    def hablar(self, palabras): pass #la palabra reservada pass indica el final de la declaración del método. Se coloca al final del método.
     
class Deportista (Persona): #Una clase derivada de una clase abstracta se denomina IMPLEMENTACIÓN: Deportista es una implementación de Persona.
    def __init__(self, edad, nombre, deporte): 
        self.edad = edad
        self.nombre = nombre 
        self.__deporte = deporte  ##MODIFIQUÉ, colocando dos guiones bajos antes del atributo, para encapsular y ocultar.    
        print ("Se ha creado a", self.nombre, "de", self.edad)
        
    def practicarDeporte(self, deporte): 
       self.__deporte = deporte 
       print (self.nombre, ": Voy a practicar")  
    
    def verMiDeporte(self): #Función para volver público el atributo deporte que previamente estaba oculto (lo sabemos porque permanecen los guiones bajos).
        return self.__deporte

    def hablar(self, *palabras): #Definición para cada método abstracto.
        for frase in palabras:
            print(self.nombre, ":", frase)  

#CÓDIGO PRINCIPAL: usará las clases ya declaradas y "funcionará" por sí mismo.
#Sólo necesitará que introduzcamos los atributos particulares de cada self = OBJETO
#juan = Persona ("17", "Juan") 
#juan.hablar ("Hola, soy Juan") 

luis = Deportista("18", "Luis", "natación") 
luis.hablar("Hola, ¿qué tal?")
#luis.practicarDeporte(luis.__deporte) #Ocultar: ACTUALICÉ el atributo, colocando los dos guiones bajos que también agregué en el apartado del método.
print(luis.nombre, ": Yo practico", luis.verMiDeporte()) #Mostrar

lalo = Deportista("30", "Lalo", "futbol") 
lalo.hablar("Hola a ambos, yo soy Lalo") 
print(lalo.nombre, ": A mi me gusta el", lalo.verMiDeporte())


