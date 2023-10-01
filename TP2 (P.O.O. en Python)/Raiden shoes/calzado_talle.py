class CalzadoTalle:

  def __init__(self, descripcion: str, medida_en_cm: float) -> None:
    self.descripcion = descripcion
    self.medida_en_cm = medida_en_cm

  def __str__(self):
    return f"descripción: {self.descripcion}, medida en cm: {self.medida_en_cm}"

  def __repr__(self):
    return "".join(self.descripcion, self.medida_en_cm)

  def __eq__(self, other: any):
    if isinstance(other, CalzadoTalle):
      if self.descripcion and self.medida_en_cm == other.descripcion and other.medida_en_cm:
        return True
      else:
        return other.descripcion, other.medida_en_cm
