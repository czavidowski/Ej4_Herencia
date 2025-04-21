from mago import Mago

class Hechicero(Mago):
    def __init__(self, nombre, edad, nivel_poder, mana):
        super().__init__(nombre, edad, nivel_poder)
        self.mana = mana

    def lanzar_hechizo(self, hechizo, costo_mana):
        if hechizo in self.hechizos:
            if self.mana >= costo_mana:
                self.mana -= costo_mana
                return f"{self.nombre} lanza {hechizo}. Maná restante: {self.mana}"
            else:
                return f"{self.nombre} no tiene suficiente maná para lanzar {hechizo}"
        return f"{self.nombre} no conoce el hechizo: {hechizo}"