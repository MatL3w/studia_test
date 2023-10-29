liczby = []

for i in range(10):
    liczba = float(input(f"Podaj liczbę {i+1}: "))
    liczby.append(liczba)

maksymalny = max(liczby)

srednia = sum(liczby) / len(liczby)

print(f"Maksymalny element w liście to: {maksymalny}")
print(f"Średnia z liczb w liście to: {srednia}")