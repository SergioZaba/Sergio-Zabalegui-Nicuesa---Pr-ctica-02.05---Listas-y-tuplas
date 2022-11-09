vocales = ["a",  "e", "i", "o", "u"]
palabra = input("Introduzca una frase y le dire el numero de veces que contiene cada vocal")

for vocales in vocales:
    veces = 0
    for i in palabra:
        if i == vocales:
            veces = veces + 1
    print("la vocal", vocales,"aparece", veces,"veces en la frase")



