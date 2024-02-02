#Optionen

farben = {
    'rot': '\033[91m',
    'grün': '\033[92m',
    'gelb': '\033[93m',
    'blau': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'zurücksetzen': '\033[0m'  # Setzt die Farbe zurück
}

# Definition von Funktionen
def ak():
    while True:
        try:
            print(
                farben['blau'] + "\033[3mAnschaffungskosten sind die Kosten, die bei der Beschaffung eines Vermögenswerts entstehen, \num ihn in einen betriebsbereiten Zustand zu versetzen. Dazu gehören der Kaufpreis des Vermögenswerts \nsowie alle mit dem Erwerb verbundenen Aufwendungen, wie beispielsweise Transportkosten, Installationskosten und rechtliche Gebühren.\033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Anschaffungskosten = Kaufpreis + Anschaffungsnebenkosten – Preisminderung" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Kaufpreis ein: "))
            zahl2 = float(input("Gib die Anschaffungsnebenkosten ein: "))
            zahl3 = float(input("Gib die Preisminderungen ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2 - zahl3
            print(farben['grün'] + f"Die Anschaffungskosten betragen {zahl1}€ + {zahl2}€ - {zahl3}€ ist {ergebnis}€" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])


def bep():
    while True:
        try:
            print(
                farben['blau'] + "\033[3mDer Break-Even-Punkt ist der Punkt, an dem die Erlöse eines Unternehmens genau den Gesamtkosten entsprechen, sodass weder Gewinn noch Verlust erzielt wird. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Break-Even-Point = Fixe Gesamtkosten / Deckungsbeitrag" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Fixen Gesamtkosten ein: "))
            zahl2 = float(input("Gib den Deckungsbeitrag ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." +
                      farben['zurücksetzen'])
                continue

            ergebnis = zahl1 / zahl2
            print(farben['grün'] + f"Der Break-Even-Point liegt bei {zahl1}€ / {zahl2}€  ist {ergebnis} Stück" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])


def db():
    while True:
        try:
            print(
                farben['blau'] + "\033[3mDer Deckungsbeitrag ist in der Betriebswirtschaftslehre der Betrag, \nder übrig bleibt, nachdem die variablen Kosten von den Umsatzerlösen abgezogen wurden. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Deckungsbeitrag = Stückpreis - variable Stückkosten" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Stückpreis ein: "))
            zahl2 = float(input("Gib die variablen Stückkosten ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." +
                      farben['zurücksetzen'])
                continue

            ergebnis = zahl1 - zahl2
            print(farben['grün'] + f"Der Break-Even-Point liegt bei {zahl1}€ / {zahl2}€  ist {ergebnis} Stück" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def dkf():
    while True:
        try:
            print(farben['blau'] + "\033[3mDie Durchschnittlichen fixen Stückkosten sind die Kosten, die in einem Unternehmen entstehen und \nauf jedes hergestellte Produkt entfallen, wobei sie unabhängig von der Produktionsmenge konstant bleiben.\033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Durchschn. fixe Stückkosten = ges. Fixe Kosten / Stückzahl" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die gesamten Fixkosten ein: "))
            zahl2 = float(input("Gib die Stückzahl ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 / zahl2
            print(farben['grün'] + f"XXX liegt bei {zahl1}€ / {zahl2}€  ist {ergebnis} Stück" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def dk():
    while True:
        try:
            print(farben['blau'] + "\033[3mDie Durchschnittlichen Stückkosten, auch als Durchschnittskosten oder Durchschnittliche Kosten pro Einheit bezeichnet,\nsind die Gesamtkosten eines Produkts oder einer Dienstleistung, die durch die Anzahl der produzierten Einheiten geteilt werden. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Durchschn. Stückkosten = Gesamtkosten / Stückzahl" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Gesamtkosten ein: "))
            zahl2 = float(input("Gib die Stückzahl ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 / zahl2
            print(farben['grün'] + f"Die Durchschn. Stückkosten liegen bei  {ergebnis} €/Stk" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def dkv():
    while True:
        try:
            print(farben['blau'] + "\033[3mDurchschnittliche variable Stückkosten sind die Kosten, die entstehen, um eine zusätzliche Einheit eines Produkts oder einer Dienstleistung herzustellen. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Durchschn. variable Stückkosten = Ges. Var. Kosten / Stückzahl" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die gesamten variablen Kosten ein: "))
            zahl2 = float(input("Gib die Stückzahl ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 / zahl2
            print(farben['grün'] + f"Die Durchschn. variable Stückkosten liegen bei  {ergebnis} €/Stk" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def du():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer durchschnittliche Grenzumsatz ist der Umsatz, den ein Unternehmen pro zusätzlich verkaufter Einheit eines Produkts oder einer Dienstleistung erzielt. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Durchschnittlicher Grenzumsatz = (Umsatz 2 – Umsatz 1) / (Produktionsmenge 2 – Produktionsmenge 1)" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Umsatz 2 ein: "))
            zahl2 = float(input("Gib die Umsatz 1 ein: "))
            zahl3 = float(input("Gib die Produktionsmenge 2 ein: "))
            zahl4 = float(input("Gib die Produktionsmenge 1 ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0 or zahl4 <0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 - zahl2) / (zahl3 - zahl4)
            print(farben['grün'] + f"Der Durchschnittlicher Grenzumsatz ist {ergebnis} €/Stück" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def fgk():
    while True:
        try:
            print(farben['blau'] + "\033[3mFertigungsgemeinkosten (auch als indirekte Fertigungskosten bezeichnet) sind die Kosten,\ndie in der Produktion eines Produkts anfallen, jedoch nicht direkt einem bestimmten Produkt zugeordnet werden können \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Fertigungsgemeinkosten = Fertigungskosten * Zuschlagssatz% /100%" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Fertigungskosten ein: "))
            zahl2 = float(input("Gib den Zuschlagssatz ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 * zahl2) / 100
            print(farben['grün'] + f"Die Fertigungsgemeinkosten liegen bei {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def fk():
    while True:
        try:
            print(farben['blau'] + "\033[3mFixe Kosten sind Kosten, die in einem Unternehmen konstant bleiben und unabhängig von der Produktionsmenge oder Verkaufsmenge sind.\nSie fallen regelmäßig an und ändern sich nicht, egal ob das Unternehmen mehr oder weniger produziert oder verkauft. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Fixe Kosten = Gesamtkosten – ( Variable Stückkosten * Stückzahl)" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Gesamtkosten ein: "))
            zahl2 = float(input("Gib die Variable Stückkosten ein: "))
            zahl3 = float(input("Gib die Stückzahl ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 - (zahl2 * zahl3)
            print(farben['grün'] + f"Die Fixen Kosten liegen bei {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def gk():
    while True:
        try:
            print(farben['blau'] + "\033[3mDie Gesamtkosten sind die Summe aller Kosten, die in einem Unternehmen zur Produktion von Gütern oder Dienstleistungen anfallen,\neinschließlich sowohl fixer Kosten (die unabhängig von der Produktionsmenge sind) als auch variabler Kosten (die von der Produktionsmenge abhängen). \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Gesamtkosten = Gesamte Fixe Kosten + Variable Stückkosten * Stückzahl" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die gesamten fixen Kosten ein: "))
            zahl2 = float(input("Gib die Variable Stückkosten ein: "))
            zahl3 = float(input("Gib die Stückzahl ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2 * zahl3
            print(farben['grün'] + f"Die Gesamtkosten sind {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def gw():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer Gewinn pro Stück ist der finanzielle Ertrag, den ein Unternehmen für jedes einzelne verkaufte Produkt oder jede Dienstleistung erzielt, nach Abzug aller Kosten und Aufwendungen.\nDieser Wert gibt an, wie profitabel die Herstellung oder der Verkauf eines einzelnen Produkts oder einer Dienstleistung ist. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Gewinn = Selbstkosten * Gewinnzuschlagssatz% /100%" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Selbstkosten ein: "))
            zahl2 = float(input("Gib die Gewinnzuschlagssatz ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 * zahl2) / 100
            print(farben['grün'] + f"Der Gewinn pro Stück ist {ergebnis} €/Stück" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def hk():
    while True:
        try:
            print(farben['blau'] + "\033[3mHerstellungskosten sind die Gesamtkosten, die bei der Produktion von Gütern oder Dienstleistungen anfallen,\nund umfassen alle direkten Materialkosten, direkten Arbeitskosten und die anteiligen Gemeinkosten, die mit der Herstellung verbunden sind. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Herstellkosten = Materialgesamtkosten + Fertigungskosten + Sondereinzelkosten" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Materialgesamtkosten ein: "))
            zahl2 = float(input("Gib die Fertigungskosten ein: "))
            zahl3 = float(input("Gib die Sondereinzelkosten ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2 + zahl3
            print(farben['grün'] + f"XXX ist {ergebnis} XXX" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def lvp():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer Listenverkaufspreis ist der vorgeschlagene oder offizielle Preis, zu dem ein Produkt oder eine Dienstleistung von einem Unternehmen an Kunden verkauft wird,\nbevor Rabatte oder Verhandlungen berücksichtigt werden. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Listenverkaufspreis (Rechnungsbetrag) = Verkaufspreis + Mehrwertsteuer" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Verkaufspreis ein: "))
            zahl2 = float(input("Gib die Mehrwertsteuer ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2
            print(farben['grün'] + f"XXX ist {ergebnis} XXX" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def mgk():
    while True:
        try:
            print(farben['blau'] + "\033[3mMaterialgemeinkosten sind indirekte Kosten, die in der Produktion anfallen und nicht direkt einem bestimmten Produkt zugeordnet werden können. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Materialgemeinkosten = Materialkosten * Zuschlagssatz% /100%" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Materialkosten ein: "))
            zahl2 = float(input("Gib den Zuschlagssatz ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 * zahl2) / 100
            print(farben['grün'] + f"Die Matrialgemeinkosten liegen bei {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def mk():
    while True:
        try:
            print(farben['blau'] + "\033[3m \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Materialkosten = Fertigungsmaterialkosten + Materialgemeinkosten" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Fertigungsmaterialkosten ein: "))
            zahl2 = float(input("Gib die Materialgemeinkosten ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2
            print(farben['grün'] + f"Die Metrialkosten liegen bei {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def mwst():
    while True:
        try:
            print(farben['blau'] + "\033[3mDie Mehrwertsteuer (MwSt) ist eine indirekte Verbrauchssteuer, die auf den Verkauf von Waren und Dienstleistungen erhoben wird und die Endverbraucher tragen. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Mehrwertsteuer = Verkaufspreis * (Merhwertsteuersatz%/100%)" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Verkaufspreis ein: "))
            zahl2 = float(input("Gib den Merhwertsteuersatz ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 * (zahl2 / 100)
            print(farben['grün'] + f"Die Mehrwertsteuer beträgt {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def nvp():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer Nettoverkaufspreis ist der Preis, den ein Unternehmen für ein Produkt oder eine Dienstleistung nach Abzug aller Rabatte,\nSkonti und Steuern erhält, und er stellt den tatsächlichen Erlös dar, den das Unternehmen aus dem Verkauf erzielt. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Nettoverkaufspreis = Selbstkosten + Gewinn" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Selbstkosten ein: "))
            zahl2 = float(input("Gib den Gewinn ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2
            print(farben['grün'] + f"XXX ist {ergebnis} XXX" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def sk():
    while True:
        try:
            print(farben['blau'] + "\033[3mDie Selbstkosten eines Produkts oder einer Dienstleistung sind die gesamten Kosten, die ein Unternehmen aufbringen muss,\num dieses Produkt herzustellen oder diese Dienstleistung zu erbringen, ohne Berücksichtigung von Gewinn oder Verlust.  \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Selbstkosten = Herstellkosten + Verwaltungs und Vertriebsgemeinkosten + Fertigungseinzelkosten + Sondereinzelkosten d. Vertriebes" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Herstellkosten ein: "))
            zahl2 = float(input("Gib die Verwaltungs und Vertriebsgemeinkosten ein: "))
            zahl3 = float(input("Gib die Fertigungseinzelkosten ein: "))
            zahl4 = float(input("Gib die Sondereinzelkosten d. Vertriebes ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 < 0 or zahl4 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 + zahl2 + zahl3 + zahl4
            print(farben['grün'] + f"Die Selbstkosten liegen bei {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def sek():
    while True:
        try:
            print(farben['blau'] + "\033[3mSondereinzelkosten sind Kosten, die speziell und eindeutig einem einzelnen Produkt oder Auftrag zugeordnet werden können\nund somit direkt und präzise den Kosten eines bestimmten Projekts oder Produkts zugeordnet werden. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Sondereinzelkosten = (MatKosten + FertKosten) * Zuschlagssatz% /100%" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Materialkosten ein: "))
            zahl2 = float(input("Gib die Fertigungkosten ein: "))
            zahl3 = float(input("Gib die Zuschlagssatz ein: "))
            if zahl1 < 0 or zahl2 < 0 or zahl3 <0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 + zahl2) * zahl3 / 100
            print(farben['grün'] + f"Die Sondereinzelkosten betragen {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def sük():
    while True:
        try:
            print(farben['blau'] + "\033[3mStückkosten sind die Gesamtkosten für die Herstellung eines einzelnen Produkts oder einer Einheit,\nerrechnet durch die Division der Gesamtkosten durch die Anzahl der hergestellten Einheiten. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Stückkosten = Gesamtkosten / Produktionsmenge" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die Gesamtkosten ein: "))
            zahl2 = float(input("Gib die Produktionsmenge ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 / zahl2
            print(farben['grün'] + f"Die Stückkosten betragen {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def us():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer Umsatz ist der Gesamtbetrag an Einnahmen,\nden ein Unternehmen durch den Verkauf von Waren oder Dienstleistungen in einem bestimmten Zeitraum erzielt hat. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Umsatz = Preis * Produktionsmenge" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Preis ein: "))
            zahl2 = float(input("Gib die Produktionsmenge ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 * zahl2
            print(farben['grün'] + f"Der Umsatz ist {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def vk():
    while True:
        try:
            print(farben['blau'] + "\033[3mVariable Kosten sind Kosten, die sich direkt proportional zur Produktionsmenge oder Verkaufsmenge eines Unternehmens ändern. \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Variable Kosten = Gesamtkosten – fixe Kosten" + farben['zurücksetzen'])
            zahl1 = float(input("Gib den Gesamtkosten ein: "))
            zahl2 = float(input("Gib die fixen Kosten ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = zahl1 - zahl2
            print(farben['grün'] + f"Die Variablen Kosten sind {ergebnis} €" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])

def ag():
    while True:
        try:
            print(farben['blau'] + "\033[3mDer Auslastungsgrad gibt an, inwieweit Produktionskapazitäten oder Ressourcen tatsächlich genutzt werden, und wird in Prozent ausgedrückt.  \033[0m" + farben['zurücksetzen'])
            print(farben['blau'] + "Formel: Auslastungsgrad = tatsächliche Produktionsmenge / höchstmögliche Produktionsmenge * 100%" + farben['zurücksetzen'])
            zahl1 = float(input("Gib die tatsächliche Produktionsmenge ein: "))
            zahl2 = float(input("Gib die höchstmögliche Produktionsmenge ein: "))
            if zahl1 < 0 or zahl2 < 0:
                print(farben['rot'] + "Negative Zahlen sind nicht erlaubt. Bitte gib gültige positive Zahlen ein." + farben['zurücksetzen'])
                continue

            ergebnis = (zahl1 / zahl2) * 100
            print(farben['grün'] + f"Der Auslastungsgrad beträgt {ergebnis} %" + farben['zurücksetzen'])
            break

        except ValueError:
            print("Ungültige Eingabe. Bitte gib gültige Zahlen ein." + farben['zurücksetzen'])


# Inhaltsverzeichnisse
alle_verzeichnis = {
    "Anschaffungskosten": ak,
    "Gewinnschwelle": bep,
    "Deckungsbeitrag": db,
    "Durchschn. fixe Stückkosten": dkf,
    "Durchschn. Stückkosten": dk,
    "Durchschn. variable Stückkosten": dkv,
    "Durchschnittlicher Grenzumsatz": du,
    "Fertigungsgemeinkosten": fgk,
    "Fixe Kosten": fk,
    "Gesamtkosten": gk,
    "Gewinn pro Stück": gw,
    "Herstellkosten": hk,
    "Listenverkaufspreis": lvp,
    "Materialgemeinkosten": mgk,
    "Materialkosten": mk,
    "Mehrwertsteuer": mwst,
    "Nettoverkaufspreis": nvp,
    "Selbstkosten": sk,
    "Sondereinzelkosten": sek,
    "Stückkosten": sük,
    "Umsatz": us,
    "Auslastungsgrad": ag,

}

kal_verzeichnis = {
    "Gewinnschwelle": bep,
    "Deckungsbeitrag": db,
    "Durchschn. fixe Stückkosten": dkf,
    "Durchschn. Stückkosten": dk,
    "Durchschn. variable Stückkosten": dkv,
    "Durchschnittlicher Grenzumsatz": du,
    "Fertigungsgemeinkosten": fgk,
    "Fixe Kosten": fk,
    "Gesamtkosten": gk,
    "Gewinn pro Stück": gw,
    "Herstellkosten": hk,
    "Listenverkaufspreis": lvp,
    "Materialgemeinkosten": mgk,
    "Materialkosten": mk,
    "Mehrwertsteuer": mwst,
    "Nettoverkaufspreis": nvp,
    "Selbstkosten": sk,
    "Sondereinzelkosten": sek,
    "Stückkosten": sük,
    "Umsatz": us,
}

mkr_verzeichnis = {
    "Anschaffungskosten": ak

}

while True:
    # Eingabeaufforderung für die gewünschte Aktion
    aktion = input(farben['gelb'] + "Gib 'Formeln' ein, um die aktuell verfügbaren Formeln anzuzeigen,\nGib 'Kategorien' ein, um alle Ketegorien zu sehen,\nGib 'Exit' ein um zu Beenden\n\nEingabe: " + farben['zurücksetzen'])

    if aktion == 'Exit':
        break  # Die Schleife beenden, wenn 'exit' eingegeben wurde

    if aktion == 'Formeln':
        # Anzeigen des Inhaltsverzeichnisses
        print(farben['magenta'] + "\033[3m\033[4m\033[1mAlle Verfügbare Formeln:\033[0m" + farben['zurücksetzen'])
        for formal_name in alle_verzeichnis:
            print(formal_name)
        continue

    if aktion == 'Kategorien':
        # Anzeigen des Inhaltsverzeichnisses
        print(farben['magenta'] + "\033[3m\033[4m\033[1mVerfügbare Kategorien:\033[0m" + farben['zurücksetzen'])
        print("Kalkulation")
        print("Maschinenkostenrechnung")
        continue

    if aktion == 'Kalkulation':
        print(farben['magenta'] + "\033[3m\033[4m\033[1mKalkulation" + farben['zurücksetzen'])
        for formal_name in kal_verzeichnis:
            print(formal_name)
        continue

    if aktion == 'Maschinenkostenrechnung':
        print(farben['magenta'] + "\033[3m\033[4m\033[1mMaschinenkostenrechnung" + farben['zurücksetzen'])
        for formal_name in mkr_verzeichnis:
            print(formal_name)
        continue

    # Die Formel basierend auf der Eingabe aufrufen, falls vorhanden
    if aktion in alle_verzeichnis:
        alle_verzeichnis[aktion]()
    else:
        print(farben['rot'] + "Ungültige Eingabe. Bitte erneut eingeben." + farben['zurücksetzen'])
