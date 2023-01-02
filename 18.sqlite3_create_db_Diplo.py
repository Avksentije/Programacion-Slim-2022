
import sqlite3 #we need to import the modules in order to define the variables


conn = sqlite3.connect("libros.db") #conn is a variable linked to the module sqlite3 and the module connect
c = conn.cursor() #Usamos el método cursor de la variable conexión conn y la conecta a la variable consulta c
#importante. el cursor va a trackear, es decir, es similar a un cursor. Sugerencia: leer en voz alta lo que hace cada parte.
#     the cursor does all the executions: CREAR nombre (columnas de la tabla y tipo de dato)

def create_table(): #def create_table(): is a fuction, because it is not associated to a class
     tabla = c.execute ('CREATE TABLE IF NOT EXISTS registros (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre VARCHAR (30) NOT NULL, autor VARCHAR (40) NOT NULL, year INTEGER (9) NOT NULL)')
     print(tabla)
     conn.commit()

create_table ()
c.close()
conn.close()

