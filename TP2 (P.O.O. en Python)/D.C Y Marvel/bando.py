class Bando:

  def __init__(self, GOOD: str, BAD: str, NEUTRAL: str, limite: int, *args):
    self.GOOD = GOOD
    self.BAD = BAD
    self.NEUTRAL = NEUTRAL
    self.limite = limite
    self.args = args

  def __str__(self):
    return f"buenos: {self.GOOD}, Malos: {self.BAD}, Neutrales: {self.NEUTRAL}, limite: {self.limite}, adicionales {self.args} "

  def __eq__(self, other):
    if isinstance(other, Bando):
      if self.GOOD and self.BAD and self.NEUTRAL and self.limite == other.GOOD and other.BAD and other.NEUTRAL and other.limite:
        return True
      else:
        return other.GOOD and other.BAD and other.NEUTRAL and other.limite
