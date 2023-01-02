#Escritura y lectura de datos, usando "w" y "r"

with open("11.Archivo.txt", 'w') as file: #¡Cuidado!, "w" sobrescribe. Para evitarlo, usar "x" o en su defecto "a".
    file.write("Soy un texto. Y voy mutando.")
    file.write("\nMe convierto en gotera.")
    file.write("\nEn un cielo en humedad.")

with open("11.Archivo.txt", 'r') as file:
    contenido = file.read()
    print(file.name, ": Dentro de un lago fluorescente.")
    print("")
    print(contenido)
    print("")
    file.close()