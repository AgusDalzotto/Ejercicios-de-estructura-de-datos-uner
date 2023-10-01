from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor
from calzado_talle import CalzadoTalle


class Calzado:

  def __init__(self, sku: int, nombre: str, descripcion: str,
               tipo: CalzadoTipo, talle: CalzadoTalle, color: CalzadoColor,
               cantidad: int, precio: float):
    try:
      if sku >= 0:
        self.sku = sku
    except ValueError:
      print("valor invalido")
    self.nombre = nombre
    self.descripcion = descripcion
    self.tipo = tipo
    self.talle = talle
    self.color = color
    try:
      if cantidad >= 0:
        self._cantidad = cantidad  # Cantidad de Existencias de este producto
    except ValueError:
      print("valor invalido")
    try:
      if precio >= 0:
        self._precio = precio
    except ValueError:
      print("valor invalido")

  def __str__(self):
    return f"sku: {self.sku}, nombre: {self.nombre}, descripcion:               {self.descripcion}, tipo: {self.tipo}, talle: {self.talle}, color:          {self.color}, cantidad: {self.cantidad}, precio: {self.precio}"

  def __repr__(self):
    return "".join(self.sku, self.nombre, self.descripcion, self.tipo,
                   self.talle, self.color, self.cantidad, self.precio)

  def __eq__(self, other: any):
    if isinstance(other, Calzado):
      if (self.sku and self.nombre and self.descripcion and self.tipo
          and self.talle and self.color and self.cantidad
          and self.precio) == (other.sku and other.nombre and other.descripcion
                               and other.tipo and other.talle and other.color
                               and other.cantidad and other.precio):
        return True
      else:
        return (other.sku, other.nombre, other.descripcion, other.tipo,
                other.talle, other.color, other.cantidad, other.precio)

  @property
  def cantidad(self):
    return self._cantidad

  @property
  def precio(self):
    return self._precio

  @property
  def total(self):
    return (self._cantidad * self._precio)
