from espiritu import Espiritu

class EspirituErrante(Espiritu):
    def __init__(self, nombre, edad, nivel_poder, afinidad_elemental, tiempo_posecion):
        super().__init__(nombre, edad, nivel_poder, afinidad_elemental)
        self.tiempo_posecion = tiempo_posecion

    def poseer(self, objetivo):
        return f"{self.nombre} posee a {objetivo} por {self.tiempo_posecion} segundos"
