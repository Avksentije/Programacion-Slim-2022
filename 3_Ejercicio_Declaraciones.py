libros = int(input("Cuantos libros lees anualmente "))

if libros > 5:
   print("Excelente, continúa así ")
if 0 < libros <= 5:
    print("Puedes mejorar, incluye un par mas ")
if libros == 0:
   print("Siempre es buen momento para comenzar ")