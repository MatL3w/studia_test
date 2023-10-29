wysokosc = int(input("Podaj wysokość trójkąta: "))

for i in range(1, wysokosc + 1):
    for k in range(i):
        print("*", end="")
    print()