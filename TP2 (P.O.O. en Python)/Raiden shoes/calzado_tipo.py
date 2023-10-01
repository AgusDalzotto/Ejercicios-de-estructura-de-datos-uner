class CalzadoTipo:

  def __init__(self, descripcion: str) -> None:
    self.descripcion = descripcion

  def __str__(self):
    return f"descripción: {self.descripcion}"

  def __repr__(self):
    return "".join(self.descripcions)

  def __eq__(self, other: any):
    if isinstance(other, CalzadoTipo):
      if self.descripcion == other.descripcion:
        return True
      else:
        return self.descripcion
