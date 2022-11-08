lista_asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
lista_nota = []
lista_resultado = []
for i in lista_asignaturas:
    nota = input("Introduzca la nota que a sacado en " + i)
    lista_nota.append(nota)
for n in range(len(lista_nota)):
    print("En " + lista_asignaturas[n] + " has sacado un " + lista_nota[n])


