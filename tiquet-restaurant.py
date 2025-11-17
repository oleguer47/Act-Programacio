IVA = 0.10
tiquet_guardat = ""
total_guardat = 0.0

def mostrar_menu():
    print("______________________________________")
    print("===== GESTIÓ COMANDES RESTAURANT =====")
    print("______________________________________")
    print("1. Crear nova comanda")
    print("2. Actualitzar comanda anterior")
    print("3. Visualitzar últim tiquet")
    print("4. Sortir")
    return input("> Tria una opció: ")

def calcular_totals(total_sense_iva):
    iva = total_sense_iva * IVA
    total_amb_iva = total_sense_iva + iva
    return iva, total_amb_iva

def crear_comanda():
    global tiquet_guardat, total_guardat
    print("______________________________________")
    print("============ NOVA COMANDA ============")
    print("______________________________________")

    nom_client = input("> Introdueix el nom del client: ")

    tiquet = f"Client: {nom_client}\n\n"
    tiquet += "Producte        Quantitat   Preu unit.   Subtotal\n"
    tiquet += "--------------------------------------------------\n"

    total_sense_iva = 0.0
    continuar = 's'

    while continuar == 's':
        producte = input("> Introdueix el producte: ")
        try:
            preu_unit = float(input("> Preu unitari (€): "))
            quantitat = int(input("> Quantitat: "))
        except ValueError:
            print("Error: Has d'introduir números vàlids per al preu i la quantitat.")
            continue

        subtotal = preu_unit * quantitat
        total_sense_iva += subtotal
        tiquet += f"{producte:<15}{quantitat:<12}{preu_unit:<12.2f}{subtotal:>7.2f} €\n"
        continuar = input("> Vols afegir un altre producte? (s/n): ").lower()

    iva, total_amb_iva = calcular_totals(total_sense_iva)
    tiquet += "--------------------------------------------------\n"
    tiquet += f"Total sense IVA:{'':>24}{total_sense_iva:>7.2f} €\n"
    tiquet += f"IVA (10%):{'':>31}{iva:>7.2f} €\n"
    tiquet += f"TOTAL A PAGAR:{'':>25}{total_amb_iva:>7.2f} €\n"
    tiquet += "==================================================\n"

    print("\nS’està generant el tiquet…\n")
    print("______________________________________")
    print("=============== TIQUET ===============")
    print("______________________________________")
    print(tiquet)
    print("Comanda enregistrada correctament.\n")

    tiquet_guardat = tiquet
    total_guardat = total_sense_iva

def actualitzar_comanda():
    global tiquet_guardat, total_guardat

    if not tiquet_guardat.strip():
        print("No hi ha cap comanda enregistrada.")
        return

    print("\n> Introdueix nous productes per afegir:")
    total_sense_iva = total_guardat
    continuar = 's'

    while continuar == 's':
        producte = input("> Introdueix un nou producte: ")
        try:
            preu_unit = float(input("> Preu unitari (€): "))
            quantitat = int(input("> Quantitat: "))
        except ValueError:
            print("Error: Has d'introduir números vàlids per al preu i la quantitat.")
            continue

        subtotal = preu_unit * quantitat
        total_sense_iva += subtotal
        tiquet_guardat += f"{producte:<15}{quantitat:<12}{preu_unit:<12.2f}{subtotal:>7.2f} €\n"
        continuar = input("> Vols afegir més productes? (s/n): ").lower()

    iva, total_amb_iva = calcular_totals(total_sense_iva)
    tiquet_guardat += "--------------------------------------------------\n"
    tiquet_guardat += f"Total sense IVA:{'':>24}{total_sense_iva:>7.2f} €\n"
    tiquet_guardat += f"IVA (10%):{'':>31}{iva:>7.2f} €\n"
    tiquet_guardat += f"TOTAL A PAGAR:{'':>25}{total_amb_iva:>7.2f} €\n"
    tiquet_guardat += "==================================================\n"

    total_guardat = total_sense_iva

    print("\nS'està actualitzant la comanda…\n")
    print("========= TIQUET ACTUALITZAT =========")
    print("______________________________________")
    print(tiquet_guardat)
    print("Comanda actualitzada correctament.\n")

def mostrar_tiquet():
    global tiquet_guardat
    if tiquet_guardat.strip():
        print("______________________________________")
        print("============ ÚLTIM TIQUET ============")
        print("______________________________________")
        print(tiquet_guardat)
    else:
        print("No hi ha cap comanda enregistrada.")

def main():
    continuar_menu = True
    while continuar_menu:
        opcio = mostrar_menu()
        match opcio:
            case "1":
                crear_comanda()
            case "2":
                actualitzar_comanda()
            case "3":
                mostrar_tiquet()
            case "4":
                print("______________________________________")
                print("========== FINS LA PROPERA! ==========")
                print("______________________________________")
                continuar_menu = False
            case _:
                print("Opció no vàlida. Torna-ho a provar.\n")

if __name__ == "__main__":
    main()
