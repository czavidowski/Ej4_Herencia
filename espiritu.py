from criatura_magica import CriaturaMagica

class Espiritu(CriaturaMagica):
    def __init__(self, nombre, edad, nivel_poder, afinidad_elemental):
        super().__init__(nombre, edad, nivel_poder)
        self.afinidad_elemental = afinidad_elemental

