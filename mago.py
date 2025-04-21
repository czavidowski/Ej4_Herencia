from individuo_magico import IndividuoMagico

class Mago(IndividuoMagico):
    def __init__(self, nombre, edad, nivel_poder):
        super().__init__(nombre, edad, nivel_poder)
        self.hechizos = []

    def aprender_hechizo(self, hechizo):
        self.hechizos.append(hechizo)

    def lanzar_hechizo(self, hechizo):
        if hechizo in self.hechizos:
            return f"{self.nombre} lanza el hechizo: {hechizo}"
        return f"{self.nombre} no conoce el hechizo: {hechizo}"
