lista = []

while True:
    materias = input("Introduzca las materias de una en una pulsando ENTER"
                     " , cuando acabe escriba YA ")
    lista.append(materias)
    if materias.upper() == "YA":
        print(lista)
        break


