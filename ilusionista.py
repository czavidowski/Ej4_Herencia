from mago import Mago

class Ilusionista(Mago):
    def __init__(self, nombre, edad, nivel_poder):
        super().__init__(nombre, edad, nivel_poder)
        self.ilusiones = []

    def aprender_hechizo(self, hechizo):
        if len(self.hechizos) < 4:
            self.hechizos.append(hechizo)
        else:
            print(f"{self.nombre} no puede aprender más de 4 hechizos")

    def crear_ilusion(self, ilusion):
        self.ilusiones.append(ilusion)
        return f"{self.nombre} crea una ilusión: {ilusion}"