from bestia_magica import BestiaMagica

class Quimera(BestiaMagica):
    def __init__(self, nombre, edad, nivel_poder, nivel_agresividad, cabezas):
        super().__init__(nombre, edad, nivel_poder, nivel_agresividad)
        self.cabezas = cabezas  # lista de habilidades por cabeza

    def usar_habilidad(self, numero_cabeza):
        if 0 <= numero_cabeza < len(self.cabezas):
            habilidad = self.cabezas[numero_cabeza]
            return f"{self.nombre} usa la habilidad de la cabeza : {habilidad}"
        return "Habilidad de cabeza no valida"
