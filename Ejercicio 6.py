# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas
# que el usuario tiene que repetir.
lista_asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
aprobadas = []

for i in lista_asignaturas:
    nota = float(input("Introduzca la nota que a sacado en " + i))
    if nota >= 5:
        aprobadas.append(i)
for aprobadas in lista_asignaturas:
        lista_asignaturas.remove(aprobadas)
print("Las asiggnaturas que tienes que repetir son=", lista_asignaturas)


