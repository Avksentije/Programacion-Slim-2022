
import sqlite3 #we need to import the modules in order to define the variables

def insertar():
    db1 = sqlite3.connect("libros.db") #conn is a variable linked to the module sqlite3 and the module connect
    print("Estás en la función insertar")

    nombre1 = input('El hombre duplicado')
    autor1 = input('Saramago')
    año1= input('1990')
    
    consulta = db1.cursor()

    strConsulta = "INSERT INTO registros (nombre, autor, year) VALUES (nombre1, autor1, año1)"
    print(strConsulta)
    consulta.execute(strConsulta)
    consulta.close()
    db1.commit
    db1.close()

insertar()

