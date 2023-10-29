import random

start_zakres = int(input("Podaj począkowy zakres: "))
end_zakres = int(input("Podaj końcowy zakres: "))
operacje = int(input("Podaj ilość działań do wykonania: "))

punkty = 0

for i in range(operacje):
    # Losuj dwie liczby
    num1 = random.randint(start_zakres, end_zakres)
    num2 = random.randint(start_zakres, end_zakres)
    
    # Oblicz poprawny wynik mnożenia
    ans = num1 * num2
    
    # Wyświetl pytanie i pobierz odpowiedź od użytkownika
    user_ans = int(input(f"Ile to jest {num1} * {num2}? "))
    
    # Sprawdź odpowiedź
    if user_ans == ans:
        print("Poprawna odp")
        punkty += 1
    else:
        print(f"Niepoprawna odp")
        punkty -= 1

# Wyświetl wynik
print(f"Twój wynik to {punkty} punktów.")