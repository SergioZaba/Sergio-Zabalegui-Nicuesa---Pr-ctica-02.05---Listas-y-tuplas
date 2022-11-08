numeros_ganadores = []
while True:
    numero = input("Introduzca los numeros de uno en uno, cuando acabe escriba YA")
    if numero.upper() == "YA":
            break
    numeros_ganadores.append(numero)
numeros_ganadores.sort()
print (numeros_ganadores)