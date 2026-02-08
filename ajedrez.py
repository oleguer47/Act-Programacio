tablero = [
    ['t','c','a','q','k','a','c','t'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['P','P','P','P','P','P','P','P'],
    ['T','C','A','Q','K','A','C','T']
]

columnas = ['a','b','c','d','e','f','g','h']

def mostrar_tablero():
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()
    print()

def convertir(coordenada):
    letra = coordenada[0]
    numero = coordenada[1]
    columna = columnas.index(letra)
    fila = 8 - int(numero)
    return fila, columna

def verificar_ganador(pieza_destino):
    if pieza_destino == 'k':
        print("Ganan las blancas")
        return True
    elif pieza_destino == 'K':
        print("Ganan las negras")
        return True
    return False

def mover(f1, c1, f2, c2):
    pieza_destino = tablero[f2][c2]
    tablero[f2][c2] = tablero[f1][c1]
    tablero[f1][c1] = '.'
    return verificar_ganador(pieza_destino)

def mover_peon(f1, c1, f2, c2):
    return mover(f1, c1, f2, c2)

def mover_torre(f1, c1, f2, c2):
    if f1 == f2 or c1 == c2:
        return mover(f1, c1, f2, c2)
    else:
        print("Movimiento invalido para torre")

def mover_caballo(f1, c1, f2, c2):
    if (abs(f1 - f2) == 2 and abs(c1 - c2) == 1) or (abs(f1 - f2) == 1 and abs(c1 - c2) == 2):
        return mover(f1, c1, f2, c2)
    else:
        print("Movimiento invalido para caballo")

def mover_alfil(f1, c1, f2, c2):
    if abs(f1 - f2) == abs(c1 - c2):
        return mover(f1, c1, f2, c2)
    else:
        print("Movimiento invalido para alfil")

def mover_reina(f1, c1, f2, c2):
    if f1 == f2 or c1 == c2 or abs(f1 - f2) == abs(c1 - c2):
        return mover(f1, c1, f2, c2)
    else:
        print("Movimiento invalido para reina")

def mover_rey(f1, c1, f2, c2):
    if abs(f1 - f2) <= 1 and abs(c1 - c2) <= 1:
        return mover(f1, c1, f2, c2)
    else:
        print("Movimiento invalido para rey")

def jugar():
    while True:
        mostrar_tablero()
        movimiento = input("(origen destino): ")

        if movimiento.lower() == "salir":
            break

        try:
            origen, destino = movimiento.split()
        except:
            print("casilla incorrecta")
            continue

        f1, c1 = convertir(origen)
        f2, c2 = convertir(destino)

        pieza = tablero[f1][c1].lower()
        fin = False

        if pieza == 'p':
            fin = mover_peon(f1, c1, f2, c2)
        elif pieza == 't':
            fin = mover_torre(f1, c1, f2, c2)
        elif pieza == 'c':
            fin = mover_caballo(f1, c1, f2, c2)
        elif pieza == 'a':
            fin = mover_alfil(f1, c1, f2, c2)
        elif pieza == 'q':
            fin = mover_reina(f1, c1, f2, c2)
        elif pieza == 'k':
            fin = mover_rey(f1, c1, f2, c2)
        else:
            print("No hay pieza en esa casilla")

        if fin:
            mostrar_tablero()
            print("Juego terminado")
            break

jugar()
