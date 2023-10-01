from typing import List
from calzado import Calzado
from calzado_tipo import CalzadoTipo
from calzado_color import CalzadoColor


class CalzadoAdmin:

  def __init__(self):
    self._lista: List[Calzado] = []

  def __str__(self):
    return f"lista de calzados: {self._lista}"

  def __eq__(self, other):
    if isinstance(other, CalzadoAdmin):
      if self._lista == other._lista:
        return True
      else:
        return other._lista

  def agregar(self, item: Calzado) -> None:
    self._lista.append(item)

  def filtrar_por_tipo(self, tipo: CalzadoTipo) -> List[Calzado]:
    tipos = []

    for i in self._lista:
      if i not in tipos:
        tipos[i] = 1
      else:
        tipos[i] += 1

    return tipos

  def filtrar_precio_entre(self,
                           desde: float = 0.00,
                           hasta: float = 0.00) -> List[Calzado]:
    precio = []

    for i in self._lista:
      if desde > 0.00 and hasta > 0.00:
        if i not in precio and desde not in precio and hasta not in precio:
          precio[i] = 1
        else:
          precio[i] += 1

    return precio

  def cantidad_productos(self) -> int:
    return self._lista

  def total_productos(self) -> float:

    total = []

    for i in self._lista:
      total = i + total

    return total
