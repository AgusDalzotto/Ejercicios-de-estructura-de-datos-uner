class Personaje:

  def __init__(self, id, nombre, bando, genero, universo) -> None:
    self.id: int
    self.nombre: str  # name
    self.bando: str  # alignment
    self.genero: str  # gender
    self.universo: str  # universe

  def __eq__(self, other):
    if isinstance(other, Personaje):
      if self.id and self.nombre and self.bando and self.genero and self.universo == other.id and other.nombre and other.bando and other.genero and other.universo:
        return True
      else:
        return other.id and other.nombre and other.bando and other.genero and other.universo

  def __str__(self):
    return f"id {self.id}, nombre: {self.nombre}, bando: {self.bando},     genero: {self.genero}, universo: {self.universo}"

  def __repr__(self):
    return "".join(self.id, self.nombre, self.bando, self.genero,
                   self.universo)
