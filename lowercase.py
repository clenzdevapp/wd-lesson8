while True:
    inputString = raw_input("Gib einen Satz ein: ")
    outputString = str.lower(inputString)
    print(outputString)
    decision = str.lower(raw_input("Weitere Eingabe? Ja / Nein "))
    if decision == "ja":
        print("...")
    else:
        break