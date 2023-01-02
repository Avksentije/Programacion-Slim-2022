import sqlite3 #we need to import the modules in order to define the variables
import time
import datetime
import random
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#from matplotlib import style
#style.use('fivethrityeight')

conn = sqlite3.connect("tania.db") 
c = conn.cursor() 

def create_table(): 
     c.execute ('CREATE TABLE IF NOT EXISTS tania (unix REAL, datastamp TEXT, keyword TEXT, value REAL)')

def dynamic_data_entry(): #into this function we define the variables to create the attributes of the entity (values of the database)
    unix = time.time() #we define the variables and the modules
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%D %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(35, 50)
    c.execute("INSERT INTO tania (unix, datastamp, keyword, value) VALUES (?,?,?,?)", (unix, date, keyword, value)) 
    conn.commit()
    c.close()
    conn.close()

#def read_from_db():
#   c.execute("SELECT * FROM tania WHERE value>=40 AND keyword ='Python'") # * means everything
   #data = c.fetchall()
   #print(data)
#   for row in c.fetchall():
#        print(row)

#def graph_data():

#read_from_db() 
#create_table ()
#for i in range (0,10) :
    #dynamic_data_entry()
    #time.sleep(1)
#c.close()
#conn.close()

