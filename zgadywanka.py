import random

secret_number = random.randint(1, 100)

attempts = 0

print("Odgadnij liczbę z zakresu od 1 do 100")

while True:
    guess = int(input("Podaj swoją próbę: "))

    attempts += 1

    if guess < secret_number:
        print("Szukana wartość jest większa.")
    elif guess > secret_number:
        print("Szukana wartość jest mniejsza.")
    else:
        print(f"Odgadłeś liczbę {secret_number} po {attempts} próbach.")
        break
