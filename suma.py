n = int(input("Podaj liczbę n: "))

total = 0

string_value = str(n)

for i in string_value:
    total += int(i)

print(f"suma:{total}")