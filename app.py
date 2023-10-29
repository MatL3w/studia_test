# print("Hello, from Python!")

# # if statement
# if 5 > 2:
#     print("Five is greater than two!")
#     print("second line")
# #indentation is crucial in python. have to be at least one space under statement
# """
# another type of comment
# """
# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# # casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# # Many Values to Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# # concatenatio 
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# # function
# def myfunc():
#   print("Python is " + x)

# myfunc()

# # global keyword
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# # type
# x = 5
# y ='string'
# print(type(x))

# if type(x) == type(x):
#   print('type(x) == type(x)')


# #  RANDOM
# import random
# print(random.randrange(1, 2137))

# straing as array
# a = "Hello, World!"
# print(a[1]) 


# Przyklad przerwania

# print("Instrukcja przerwania:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Wewnatrz petli.", i)
# print("Poza petla.")


# # Przyklad wznawiania

# print("\nInstrukcja wznowienia:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Wewnatrz petli.", i)

# #  for with string 
# for litera in "lol":
#     print(litera)

# x=1277
# x = 1 & x
# print(x)

# liczby = [10, 5, 7, 2, 1]
# print("Zawartość listy:", liczby) # wyświetlanie oryginalnej zawartości listy

# liczby[0] = 111
# print("\nPoprzednia zawartość listy:", liczby) # wyświetlanie poprzedniej zawartości listy

# liczby[1] = liczby[4] # kopiowanie wartości piątego elementu do drugiego
# print("Poprzednia zawartość listy:", liczby) # wyświetlanie poprzedniej zawartości listy

# print("\nDługość listy:", len(liczby)) # wyświetlanie długości listy

# del liczby[0]
# print(liczby)

# liczby = [111, 7, 2, 1]
# print(liczby[-1])
# print(liczby[-2])
# x=input('lol:')
# print(x)
# print('len:',len(liczby))
# liczby.

# liczby = [111, 7, 2, 1]
# print(len(liczby))
# print(liczby)

# ###

# liczby.append(4)

# print(len(liczby))
# print(liczby)

# ###

# liczby.insert(0, 222)
# print(len(liczby))
# # print(liczby)
# moja_lista = [] # Tworzenie pustej listy.

# for i in range(5):
#     moja_lista.insert(0, i + 1)

# print(moja_lista)

# moja_lista = [10, 1, 8, 3, 5]
# suma = 0

# for i in range(len(moja_lista)):
#     suma += moja_lista[i]

# # print(suma)
# my_list = [5, 2, 8, 1, 3]
# my_list.sort()  # Sorts the list in place
# print(my_list)  # Output: [1, 2, 3, 5, 8]

# my_list = ["apple", "banana", "cherry", "date",1,2]
# string_list = list(map(str, my_list))
# sorted_list = sorted(string_list)
# print(sorted_list)  # Output: ['date', 'cherry', 'banana', 'apple']

# # Kopiowanie części listy.
# lista = [10, 8, 6, 4, 2]
# nowa_lista = lista[0:3]
# print(nowa_lista)

# lista = [0, 3, 12, 8, 2]

# print(5 in lista)
# print(5 not in lista)
# print(12 in lista)
# x=11
# y=4
# x =x % y
# x =x % y
# print(x)

# t =[[3-i for i in range (3)] for j in range (3)]
# s=0
# for i in range (3):
#     s+= t[i][i]
# print(s)
    
# lst = [1,2,3,4]
# print(lst[-3:-2])
# c= 1 & 0
# d= 1 | 0
# e = 1 ^0
# print (c+d+e)

# nums =[1,2,3]
# vals = nums[-1:-2]
# print(vals)

# x = 1 
# x=x==x
# print(x)

# for i in range(1):
#     print("x")
# else:
#     print("x")
    
# print(0%2)
# lst =[[0,1,2,3] for i in range(2)]
# print(lst[2][0])
# d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
# d2 = {'Mary Louis':'A', 'Patrick White':'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)

# lst = ["car", "Ford", "flower", "Tulip"]

# tup = tuple(lst)
# print(tup)

# colors = {
#     "white" : (255, 255, 255),
#     "grey"  : (128, 128, 128),
#     "red"   : (255, 0, 0),
#     "green" : (0, 128, 0)
#     }

# for col, rgb in colors.items():
#     print(col, ":", rgb)

## przekazywanie argumentow pozycyjnych 

# def przedstawienie(imie, nazwisko):
#     print("Cześć, nazywam się", imie, nazwisko)

# przedstawienie(imie = "James", nazwisko = "Bond")
# przedstawienie(nazwisko = "Skywalker", imie = "Luke")

# def suma(a, b=2, c=1):
#     print(a + b + c)

# suma(a=1, c=3)
# def test_zakresu():
#     x = 123

# def moja_funkcja():
#     print("Czy znam tę zmienną?", var)


# var = 1
# moja_funkcja()
# print(var)

# def moja_funkcja():
#     global var
#     var = 2
#     print("Czy znam tę zmienną?", var)


# var = 1
# moja_funkcja()
# print(var)



# # Pobierz czas w sekundach od użytkownika
# czas_w_sekundach = int(input("Podaj czas w sekundach: "))

# # Oblicz godziny, minuty i pozostałe sekundy
# godziny = czas_w_sekundach // 3600
# czas_w_sekundach %= 3600
# minuty = czas_w_sekundach // 60
# sekundy = czas_w_sekundach % 60

# # Wyświetl przeliczony czas
# print(f"Czas: {godziny} godzin, {minuty} minut, {sekundy} sekund")

n = int(input("Podaj wymiar czekolady n: "))
m = int(input("Podaj wymiar czekolday m: "))
k = int(input("Podaj ilosc wyllamanych czesci czekolady: "))

wynik = (k == n or k == m)
if wynik:
    print("mozna")
else:
    print("nie mozna")