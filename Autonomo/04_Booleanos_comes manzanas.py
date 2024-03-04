#Booleanos

a = int(input("¿Cuántas frutas comes a la semana (introduce un número): "))

if a == 0:
  print("Ingiere al menos cinco por semana, confiamos en ti.")
if a in range(0,11):
  print("Buen trabajo, te estás nutriendo bien.")
else :
  print("Vas muy bien. Procura no exceder más de 15 frutas por semana, para evitar exceso de azúcar.")