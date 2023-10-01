from typing import Optional


class CalzadoColor:

  def __init__(self, primario: str) -> None:
    self.primario = primario
    self.secundario = Optional[str]

  def __str__(self):
    return f"color primario: {self.primario}, color secundario: {self.secundario}"

  def __repr__(self):
    return "".join(self.primario, self.secundario)

  def __eq__(self, other):
    if isinstance(other, CalzadoColor):
      if self.primario and self.secundario == other.primario and other.secundario:
        return True
      else:
        return other.primario, other.secundario
