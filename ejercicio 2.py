lista = []

while True:
    materias = input("Introduzca las materias de una en una pulsando ENTER"
                     " , cuando acabe escriba YA ")

    if materias.upper() == "YA":
        for i in lista:
            print("Yo estudio", i,"donde", i,"es cada una de las asignaturas de la lista")
        break

    lista.append(materias)