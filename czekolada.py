n = int(input("Podaj wymiar czekolady n: "))
m = int(input("Podaj wymiar czekolday m: "))
k = int(input("Podaj ilosc wyllamanych czesci czekolady: "))

wynik = (((n*m)%k) == 0)
if wynik:
    print("mozna")
else:
    print("nie mozna")i