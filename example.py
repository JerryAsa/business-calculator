def Vorlage():
    while True:
        try:
            print(farben['blau'] + "\033[3m \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel:" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den XXX ein: "))
            zahl2 = float(input("Gib die XXX ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 - zahl2
            print(farben['grün'] + f"XXX ist {ergebnis} XXX" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])
