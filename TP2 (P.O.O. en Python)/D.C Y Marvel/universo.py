class Universo:

  def __init__(self, MARVEL, DC, *args):
    self.MARVEL = MARVEL
    self.DC = DC
    self.args = args

  def __str__(self):
    return f"Marvel: {self.MARVEL}, DC: {self.DC}, adicionales: {self.args}"

  def __eq__(self, other: any):
    if isinstance(other, Universo):
      if self.MARVEL and self.DC == other.MARVEL and other.DC:
        return True
      else:
        return other.MARVEL and other.DC
