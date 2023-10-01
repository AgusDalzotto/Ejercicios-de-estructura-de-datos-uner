class Genero:

  def __init__(self, FEMALE: str, MALE: str, *args):
    self.FEMALE = FEMALE
    self.MALE = MALE
    self.args = args

  def __str__(self):
    return f"Femenino {self.FEMALE}, Masculino: {self.MALE}, adicionales: {self.args}"

  def __eq__(self, other):
    if isinstance(other, Genero):
      if self.MALE and self.FEMALE == other.MALE and other.FEMALE:
        return True
      else:
        return other.MALE, other.FEMALE
