import random

FINAL = 63
OQUES = [5, 9, 14, 18, 23, 27, 32, 36, 41, 45, 50, 54, 59]
PONTS = [6, 12]

def demanar_numero_jugadors():
    numero = 0
    while numero < 2 or numero > 4:
        numero = int(input("Introdueix el numero de jugadors (2-4): "))
    return numero

def crear_jugadors(numero):
    jugadors = []
    for i in range(numero):
        nom = input(f"Nom del jugador {i+1}: ")
        jugadors.append([nom, 0, 0, True])  
    return jugadors

def tirar_daus(posicio):
    if posicio >= 60:
        num_daus = 1
    else:
        num_daus = 2
    tirada = []
    for i in range(num_daus):
        tirada.append(random.randint(1,6))
    if num_daus == 2:
        suma = tirada[0] + tirada[1]
        print(tirada[0], "i", tirada[1], "=", suma)
    else:
        suma = tirada[0]
        print(tirada[0])
    return suma, tirada

def controlar_exces(posicio):
    if posicio > FINAL:
        posicio = FINAL - (posicio - FINAL)
    return posicio

def casella_especial(jugador, tirada_daus):
    repetir = False
    pos = jugador[1]

    if pos in OQUES:
        print("Casella", pos, ": Oca.")
        print("De oca a oca i tiro porque me toca.")
        jugador[1] = OQUES[OQUES.index(pos) + 1] # busca la seguent oca
        repetir = True
    elif pos in PONTS:
        print("Casella", pos, ": Pont.")
        print("De puente a peunte i tiro porque me lleva la corriente.")
        jugador[1] = 12 if pos == 6 else 6
        repetir = True
    elif pos == 19:
        print("Casella 19: Fonda. Perds un torn.")
        jugador[2] = 1
    elif pos == 31:
        print("Casella 31: Pou. Perds dos torns.")
        jugador[2] = 2
    elif pos == 42:
        print("Casella 42: Laberint. Tornes a la casella 39.")
        jugador[1] = 39
    elif pos == 52:
        print("Casella 52: Preso. No pots moure't durant tres torns.")
        jugador[2] = 3
    elif pos == 58:
        print("Casella 58: La mort. Tornes al principi.")
        jugador[1] = 0

    if jugador[3] and sorted(tirada_daus) in ([3,6],[4,5]):
        jugador[1] = 26 if sorted(tirada_daus) == [3,6] else 53
        print("De dau a dau i tiro perque em toca.")
        repetir = True

    jugador[3] = False
    return repetir

def torn_jugador(jugador):
    if jugador[2] > 0:
        jugador[2] -= 1
        print("No pots tirar aquest torn.")
        return False
    input(" tirar")
    suma, tirada = tirar_daus(jugador[1])
    jugador[1] += suma
    jugador[1] = controlar_exces(jugador[1])
    repetir = casella_especial(jugador, tirada)
    print("Estas a la casella", jugador[1])
    return repetir

def joc_oca():
    numero = demanar_numero_jugadors()
    jugadors = crear_jugadors(numero)
    torn = 0
    acabat = False

    while not acabat:
        print("\n" + "_"*40)
        print("Torn del jugador", torn+1, ":", jugadors[torn][0])
        repetir = torn_jugador(jugadors[torn])
        if jugadors[torn][1] == FINAL:
            print("\n", jugadors[torn][0], "ha guanyat el joc!")
            acabat = True
        if not repetir:
            torn = (torn + 1) % numero

joc_oca()
