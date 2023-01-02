pregunta = str(input("¿Trabajas desde casa? (si/no): "))

if pregunta == "si":
    print("Cool!")

if pregunta == "no":
    print("Está cool, sin embargo, vamos a hablar del traslado")

    tiempo = input("¿Cuánto tiempo dura tu trayecto al trabajo: introduce la cantidad de minutos en número: " )
    if tiempo == "0":
        print("¿En serio? Teletransportación XD")
    else :
        print("Recuerda tener todo listo con 15 min de anticipación. Prevee retrasos o tráfico")