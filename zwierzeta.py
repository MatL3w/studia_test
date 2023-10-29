zwierzeta = []

for _ in range(7):
    zwierze = input("nowe zwierze: ")
    zwierzeta.append(zwierze)

print("Zwierzeta na k:")
for zwierze in zwierzeta:
    if zwierze.lower().startswith("k"):
        print(zwierze)

print("Zwierzęta z przynamniej 3 znakami w nazwie:")
for zwierze in zwierzeta:
    if len(zwierze) >= 3:
        print(zwierze)

zwierzeta.reverse()

print("Wszystkie zwierzęta (odwrócona lista):", zwierzeta)

najczestsza_litera_o = None
najczestsza_liczba_o = 0
najczestsze_zwierze = None

for zwierze in zwierzeta:
    liczba_o = zwierze.lower().count("o")
    if liczba_o > najczestsza_liczba_o:
        najczestsza_litera_o = "o"
        najczestsza_liczba_o = liczba_o
        najczestsze_zwierze = zwierze

if najczestsza_litera_o:
    print(f"Zwierzę, w którego nazwie najczęściej występuje litera 'o', to: {najczestsze_zwierze}")
else:
    print("Brak zwierząt z literą 'o' w nazwie.")