# coding=utf8
print("""Hallo User!
Ziel dieses Programms ist es, Kilometer in Meilen umzuwandeln und anzuzeigen.
""")
while True:
    inputKilometer = int(raw_input("Bitte gib die Kilometeranzahl ein: "))
    miles = inputKilometer * 0.621371
    outputMiles = str(inputKilometer) + " Kilometer = " + str(miles) + " Meilen"
    print(outputMiles)

    decision = raw_input("""
Soll eine weitere Umwandlung durchgeführt werden? Ja / Nein """)

    if decision == "Ja":
        print("""...
...
...""")
    else:
        print("""
Vielen Dank für die Benutzung dieses Programms. Auf Wiedersehen!""")
        break