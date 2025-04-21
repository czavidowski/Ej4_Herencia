from individuo_magico import IndividuoMagico
class CriaturaMagica(IndividuoMagico):
    def __init__(self, nombre, edad, nivel_poder):
        super().__init__(nombre, edad, nivel_poder)

    def __str__(self):
        return f"{self.nombre} (Poder: {self.nivel_poder})"