import random

wylosowane_liczby = []

while len(wylosowane_liczby) < 6:
    losowa_liczba = random.randint(1, 49)
    if losowa_liczba not in wylosowane_liczby:
        wylosowane_liczby.append(losowa_liczba)

wylosowane_liczby.sort()

print("liczby:", wylosowane_liczby)