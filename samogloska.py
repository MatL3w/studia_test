
litera = input("Wprowadź literę: ")


litera = litera.lower()

if litera.isalpha():
    if litera in 'aeiouy':
        print("samogłoska.")
    else:
        print("spółgłoska.")
else:
    print("to nie litera")