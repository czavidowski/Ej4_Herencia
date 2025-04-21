from bestia_magica import BestiaMagica

class Dragon(BestiaMagica):
    def __init__(self, nombre, edad, nivel_poder, nivel_agresividad, resistencia_elemental):
        super().__init__(nombre, edad, nivel_poder, nivel_agresividad)
        self.resistencia_elemental = resistencia_elemental

    def escupir_fuego(self):
        return f"{self.nombre} escupe fuego con resistencia a {self.resistencia_elemental}"
