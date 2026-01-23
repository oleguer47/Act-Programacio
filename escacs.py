tablero = [
    ['t','c','a','q','k','a','c','t'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['P','P','P','P','P','P','P','P'],
    ['T','C','A','K','Q','A','C','T']
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

def mover_peon(origen, destino):
    f1, c1 = convertir(origen)
    f2, c2 = convertir(destino)
    tablero[f2][c2] = tablero[f1][c1]
    tablero[f1][c1] = '.'

def jugar():
    while True:
        mostrar_tablero()
        movimiento = input("(casilla de su posicion) (casilla donde la quieres mover): ")

        if movimiento.lower() == "salir":
            break

        try:
            origen, destino = movimiento.split()
        except:
            print("casilla incorrecta")
            continue

        mover_peon(origen, destino)

jugar()
