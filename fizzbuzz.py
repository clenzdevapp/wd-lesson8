inputNumber = int(raw_input("Gib eine Nummer zwischen 1 und 100 ein:"))
i = 1
while i <= inputNumber:
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
    i = i + 1