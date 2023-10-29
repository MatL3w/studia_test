# Pobierz czas w sekundach od użytkownika
czas_w_sekundach = int(input("Podaj czas w sekundach: "))

# Oblicz godziny, minuty i pozostałe sekundy
godziny = czas_w_sekundach // 3600
czas_w_sekundach %= 3600
minuty = czas_w_sekundach // 60
sekundy = czas_w_sekundach % 60

# Wyświetl przeliczony czas
print(f"Czas: {godziny} g, {minuty} m, {sekundy} s")