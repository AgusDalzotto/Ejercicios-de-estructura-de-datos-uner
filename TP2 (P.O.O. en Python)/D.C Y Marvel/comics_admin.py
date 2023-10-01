from bando import Bando
from genero import Genero
from universo import Universo
from typing import List, Tuple
from personaje import Personaje
with open("marvel_dc_characters.csv", "rt", encoding="UTF-8") as ruta:
  ruta = ruta.read()


class ComicsAdmin:

  def __init__(self):
    self._lista: List[Personaje] = []

  def agregar_desde_csv(self, ruta: str) -> None:

    agregar = 0

    for i in ruta:
      agregar = ruta.split("DC" or "Marvel")
      self._lista.append(agregar)

  def __str__(self):
    return f"lista de personajes: {self._lista}"

  def filtrar_por_bando(self,
                        bando: Bando,
                        limite: int = 0) -> List[Personaje]:

    bandos = []
    if limite >= 0:
      for i in limite:
        for i in ruta:
          if i == bando.GOOD:
            if i not in bandos:
              bandos[i] = 1
            else:
              bandos[i] += 1
          if i == bando.NEUTRAL:
            if i not in bandos:
              bandos[i] = 1
            else:
              bandos[i] += 1
          if i == bando.BAD:
            if i not in bandos:
              bandos[i] = 1
            else:
              bandos[i] += 1

      return bandos[0:limite]

  def filtrar_por_genero(self,
                         genero: Genero,
                         limite: int = 0) -> List[Personaje]:
    generos = {}

    for i in limite:
      if limite >= 0:
        for i in ruta:
          if not i == genero.MALE:
            generos[i] = 1
          else:
            generos[i] += 1
          if not i == genero.FEMALE:
            generos[i] = 1
          else:
            generos[i] += 1

    return generos[0:limite]

  def contar_por_universo(self) -> Tuple[int, int]:
    universo = {}

    for i in ruta:
      if not i == "Marvel":
        universo[i] = 1
      else:
        universo[i] += 1

      if not i == "DC":
        universo[i] = 1
      else:
        universo[i] += 1

    return universo
