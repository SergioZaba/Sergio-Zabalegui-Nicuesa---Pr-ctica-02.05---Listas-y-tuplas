lista = []
lista_nota = []
lista_impresion = []
while True:
    materias = input("Introduzca las materias de una en una pulsando ENTER"
                     " , cuando acabe escriba YA ")

    if materias.upper() == "YA":
        for i in lista:
            print("Introduzca su nota en", i)
            nota = input()
            lista_nota.append(nota)
            for e in lista_nota:
                impresion = ("En la asignatura", i, "has sacado un", e)
                lista_impresion.append(impresion)
        break

    lista.append(materias)
print(*lista_impresion)
