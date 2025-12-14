
DIGITS_HEX = "0123456789ABCDEF"


def detectar_base(cadena):
    """Retorna (base, numero_sense_prefix) o (None, None) si no es valid."""
    cadena = cadena.strip().upper()

    if cadena.startswith("0B"):
        base = 2
        num = cadena[2:]
    elif cadena.startswith("0O"):
        base = 8
        num = cadena[2:]
    elif cadena.startswith("0X"):
        base = 16
        num = cadena[2:]
    else:
        base = 10
        num = cadena

    if num == "":
        return None, None

    valids = DIGITS_HEX[:base]
    for c in num:
        if c not in valids:
            return None, None

    return base, num


def a_decimal(num_str, base):
    """Converteix una cadena numerica en base donada a enter decimal."""
    num_str = num_str.upper()
    valor = 0
    for c in num_str:
        valor = valor * base + DIGITS_HEX.index(c)
    return valor


def de_decimal_a_base(n, base):
    """Converteix un enter decimal a una cadena en la base indicada."""
    if n == 0:
        return "0"
    resultat = ""
    while n > 0:
        residu = n % base
        resultat = DIGITS_HEX[residu] + resultat
        n //= base
    return resultat


def mostrar_resultats(decimal):
    binari = de_decimal_a_base(decimal, 2)
    octal = de_decimal_a_base(decimal, 8)
    hexa = de_decimal_a_base(decimal, 16)

    print(f"Decimal: {decimal}")
    print(f"Binari: 0b{binari}")
    print(f"Octal: 0o{octal}")
    print(f"Hexadecimal: 0x{hexa}")


def main():
    while True:
        entrada = input("Introdueix un numero (o ENTER per sortir): ")
        if entrada.strip() == "":
            break

        base, num = detectar_base(entrada)
        if base is None:
            print("Error: numero o prefix no valid. Torna-ho a provar.\n")
            continue

        try:
            decimal = a_decimal(num, base)
        except Exception:
            print("Error en la conversió. Torna-ho a provar.\n")
            continue

        mostrar_resultats(decimal)
        print() 


if __name__ == "__main__":
    main()
