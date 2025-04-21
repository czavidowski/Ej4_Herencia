from mago import Mago
from criatura_magica import CriaturaMagica
class Invocador(Mago):
    def __init__(self, nombre, edad, nivel_poder):
        super().__init__(nombre, edad, nivel_poder)
        self.criaturas_invocables = []

    def invocar_criatura(self, criatura):
        if isinstance(criatura, CriaturaMagica):
            self.criaturas_invocables.append(criatura)
            return f"{self.nombre} invoca a {criatura.nombre}"