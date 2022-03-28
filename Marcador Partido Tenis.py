print("PARTIDO DE TENIS CON RESULTADO ALEATORIO")

def uniforme(): # FUNCION DE NÚMERO ALEATORIO (pseudo-aleatorio)
    global z
    a,m = 16807, 2147483647
    q = m//a
    r = m%a
    gamma = a*(z % q)-r*(z//q)
    if gamma > 0:
        z = gamma
    else:
        z = gamma + m
    return z/m

def ponerACero(): #PONER A CERO
    a,b = 0,0
    return a,b

def mostrarResultadoFinal(setsA,setsB): #RESULTADO FINAL
    print(" RESULTADOS ")
    print("Jugador A")
    print(setsA)
    print("Jugador B")
    print(setsB)
    if setsA>setsB:
        print("Ha ganado el Jugador A")
    else:
        print("Ha ganado el Jugador B")

def setFinalizado(juegosA,juegosB): #FIN SET
    return ((juegosA>=6)|(juegosB>=6))

def disputaJuego(pelotasA,pelotasB): #JUEGO EN CURSO
    while not(juegoFinalizado(pelotasA,pelotasB)):
        if bolaParaA():
            pelotasA,pelotasB = actualizaPelotas(pelotasA,pelotasB)
        #Numeración típica del tenis
        else:
            pelotasB,pelotasA = actualizaPelotas(pelotasB,pelotasA)

        representaPelotas(pelotasA,pelotasB)
    return pelotasA,pelotasB

def actualizaJuego(juegosA,juegosB,pelotasA,pelotasB):
    if pelotasA > pelotasB:
        juegosA += 1
    elif pelotasA < pelotasB:
        juegosB += 1
    return juegosA,juegosB

def disputaSet(setsA,setsB):
    juegosA,juegosB = ponerACero()
    while not(setFinalizado(juegosA,juegosB)):
        representaJugadores()
        pelotasA,pelotasB = ponerACero()
        pelotasA,pelotasB = disputaJuego(pelotasA,pelotasB)
        juegosA,juegosB = actualizaJuego(juegosA,juegosB,pelotasA,pelotasB)
    setsA,setsB = actualizaSet(setsA,setsB,juegosA,juegosB)
    print("Set finalizado",setsA,setsB)
    return setsA,setsB

def representaJugadores():
    print("Jugador A: ")
    print("Jugador B: ")

def bolaParaA():
    return uniforme() > 0.5

def actualizaSet(setsA,setsB,juegosA,juegosB):
    if juegosA > juegosB:
        setsA += 1
        print("Set para A: ",setsA)
    elif juegosB > juegosA:
        setsB += 1
        print("Set para B: ",setsB)
    return setsA,setsB

def actualizaPelotas(pelota1,pelota2):
    if pelota1 == 0:
        pelota1 = 15
    elif pelota1 == 15:
        pelota1 =30
    elif pelota1 == 30:
        pelota1 = 40
    elif pelota1 == 40:
        pelota1 = 41
    elif pelota1 == 41:
        pelota1 = 42
    if pelota2 ==41:
        pelota1 = 40
        pelota2 = 40
    return pelota1,pelota2

def partidoTerminado(setsA,setsB):
    print("Partido Terminado: ", setsA, setsB)
    return (setsA == 3) | (setsB == 3)

def juegoFinalizado(pelotasA,pelotasB):
    print("Punto Finalizado: ", pelotasA, pelotasB)
    return (((pelotasA == 41) & (pelotasB <= 30)) | ((pelotasB == 41) & (pelotasA <= 30)) |
             (pelotasA == 42) | (pelotasB == 42))

def representaPelotas(pelotasA,pelotasB):
    print(pelotasA,pelotasB)

def jugarPartido():
    setsA,setsB = ponerACero()
    while not(partidoTerminado(setsA,setsB)):
        setsA,setsB = disputaSet(setsA,setsB)
        print("Pasamos a disputar set: ",setsA,setsB)
    mostrarResultadoFinal(setsA,setsB)

z = 1
jugarPartido()