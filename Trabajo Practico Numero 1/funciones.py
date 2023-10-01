# Indicar integrantes del grupo
# Programar aquí los ejercicios desde 1 hasta 4 inclusive.
"""El trabajo fue realizado por Agustin Dalzotto"""


def factorial(numero):
    int(numero)
    n = 1
    for i in range(1, numero, 1):
        while n <= numero:
            print(numero * n)
            n = n + 1


def suma_digitos(numero):
    a = numero
    sumar = 0
    while a > 0:
        sumar = sumar + (a % 10)
        a = a // 10
    return sumar


def suma_lista(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma


def es_multiplo(n, m):
    if (n % m == 0):
        return True
    else:
        return False
