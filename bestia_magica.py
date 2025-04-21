from criatura_magica import CriaturaMagica

class BestiaMagica(CriaturaMagica):
    def __init__(self, nombre, edad, nivel_poder, nivel_agresividad):
        super().__init__(nombre, edad, nivel_poder)
        self.nivel_agresividad = nivel_agresividad

    def ataque_magico(self):
        return f"{self.nombre} realiza un ataque mágico con agresividad {self.nivel_agresividad}"
