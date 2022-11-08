# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas
# que el usuario tiene que repetir.
lista_asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
lista_nota = []
lista_resultado = []
for i in lista_asignaturas:
    nota = int(input("Introduzca la nota que a sacado en " + i))
    lista_nota.append(nota)
for n in range(len(lista_nota)):
    if lista_nota[n] < 5:
        print("En " + lista_asignaturas[n] + " has sacado un " + lista_nota[n])


