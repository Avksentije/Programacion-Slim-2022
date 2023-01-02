#ENCAPSULAMIENTO Y OCULTACIÓN

class Persona:
    def __init__(self, edad, nombre): 
        self.edad = edad
        self.nombre = nombre 
        print ("Se ha creado a", self.nombre, "de", self.edad)
    
    def hablar(self, palabras): 
        print (self.nombre, ":", palabras) 

class Deportista (Persona): 
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
      

#CÓDIGO PRINCIPAL: usará las clases ya declaradas y "funcionará" por sí mismo.
#Sólo necesitará que introduzcamos los atributos particulares de cada self = OBJETO
juan = Persona ("17", "Juan") 
juan.hablar ("Hola, soy Juan") 

luis = Deportista("18", "Luis", "natación") 
luis.hablar("Hola, ¿qué tal?")
#luis.practicarDeporte(luis.__deporte) #Ocultar: ACTUALICÉ el atributo, colocando los dos guiones bajos que también agregué en el apartado del método.
print(luis.nombre, ": Yo practico", luis.verMiDeporte()) #Mostrar

lalo = Deportista("30", "Lalo", "futbol") 
lalo.hablar("Hola a ambos, yo soy Lalo") 
print(lalo.nombre, ": A mi me gusta el", lalo.verMiDeporte())


#Cuando corro el código principal aparece AtributeError: "Deportista" object has no attibute "__deporte" y es verdad, PORQUE LOS DOS GUIONES LO VUELVEN PRIVADO.
#En seguida lo que hice (y ya aparece como modificación) es volver PÚBLICO el argumento con la función verMiDeporte().
