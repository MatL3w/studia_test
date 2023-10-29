
number_str = input("Podaj liczbę całkowitą: ")


total = 0

for i in number_str:
    total += int(i)

print(f"suma:{total}")