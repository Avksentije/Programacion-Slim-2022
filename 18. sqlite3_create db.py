
import sqlite3 #we need to import the modules in order to define the variables
import time
import datetime
import random

conn = sqlite3.connect("novela.db") #conn is a variable linked to the module sqlite3 and the module connect
c = conn.cursor() #Usamos el método cursor de la variable conexión conn y la conecta a la variable consulta c
#importante. el cursor va a trackear, es decir, es similar a un cursor. Sugerencia: leer en voz alta lo que hace cada parte.

def create_table(): #def create_table(): is a fuction, because it is not associated to a class
     c.execute ('CREATE TABLE IF NOT EXISTS miprimeratabla (unix REAL, datastamp TEXT, keyword TEXT, value REAL)')
#     the cursor does all the executions: CREAR nombre (columnas de la tabla y tipo de dato)

#https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python

def dynamic_data_entry(): #into this function we define the variables to create the attributes of the entity (values of the database)
    unix = time.time() #we define the variables and the modules
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%D %H:%M:%S'))
    keyword = 'Phyton'
    value = random.randrange(35, 50)
    c.execute("INSERT INTO miprimeratabla (unix, datastamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value)) 
    conn.commit()

create_table ()
for i in range (0,10) :
    dynamic_data_entry()
    time.sleep(1)
c.close()
conn.close()

