## Programar aquí los ejercicios desde 5 hasta 6 inclusive.

with open("marvel_dc_characters.csv", "rt", encoding="UTF-8") as file:
  linea = file.read().split(",")

diccionario = {}


def cantidad_por_bando():
  for i in linea:
    if i == "Good":
      if i not in diccionario:
        diccionario[i] = 1
      else:
        diccionario[i] += 1
    if i == "Bad":
      if i not in diccionario:
        diccionario[i] = 1
      else:
        diccionario[i] += 1
    if i == "Neutral":
      if i not in diccionario:
        diccionario[i] = 1
      else:
        diccionario[i] += 1

  return diccionario
