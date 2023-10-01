# Programar aquí los ejercicios desde 5 hasta 6 inclusive.


def filtrar_menores(lista, k):
    menores = lista[0]
    for i in range(0, len(lista)):
        if lista[i] <= k:
            menores = lista[i]
            print(menores)


def minimo_maximo(lista):
    maximo = lista[0]
    minimo = lista[0]

    for i in lista:
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i

    valores = (minimo, maximo)
    return valores
