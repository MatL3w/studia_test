x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

if x > 0 and y > 0:
    print("Punkt w 1 ćwiartce.")
elif x < 0 and y > 0:
    print("Punkt w 2 ćwiartce.")
elif x < 0 and y < 0:
    print("Punkt w 3 ćwiartce.")
elif x > 0 and y < 0:
    print("Punkt w 4 ćwiartce.")
elif x == 0 and y == 0:
    print("Punkt 0,0")
else:
    print("blad")