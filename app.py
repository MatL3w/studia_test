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
x=11
y=4
x =x % y
x =x % y
print(True)