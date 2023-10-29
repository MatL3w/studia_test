
n = int(input("Podaj liczbę n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        product = i * j
        print(f"{product}", end="\t")
    print() 