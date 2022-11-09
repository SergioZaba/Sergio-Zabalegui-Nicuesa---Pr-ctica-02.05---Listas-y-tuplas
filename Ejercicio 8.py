palabra = input("Introduzca una palabra y le dire si es un palindromo")

lista1 = []
lista2 =[]
for i in palabra:
    lista1.append(i)
for o in palabra[::-1]:
    lista2.append(o)
if lista1 == lista2:
    print("ES UN PALINDROMO")
else:
    print("NO ES UN PALINDROMO")

