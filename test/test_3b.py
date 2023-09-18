bokstav = input("skriv en bokstav: ")
if bokstav == "a" or bokstav == "A":
    print("alfabetets första bokstav")
elif bokstav.lower() == "ö":
    print("alfabetets sista bokstav")
else:
    print("ej a eller ö")