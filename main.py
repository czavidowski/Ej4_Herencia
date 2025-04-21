# main.py
from invocador import Invocador
from dragon import Dragon
from quimera import Quimera
from espiritu_errante import EspirituErrante
from hechizero import Hechicero
from ilusionista import Ilusionista

print("\n=== ️HECHICERO===")
merlin = Hechicero("Merlín", 150, 90, mana=100)
merlin.aprender_hechizo("Bola de fuego")
merlin.aprender_hechizo("Telequinesis")
print(f"Conjuros conocidos: {merlin.hechizos}")
print(merlin.lanzar_hechizo("Bola de fuego", 30))
print(merlin.lanzar_hechizo("Relámpago", 30))

print("\n===ILUSIONISTA===")
illusion = Ilusionista("Mysterio", 70, 50)
illusion.aprender_hechizo("Encantamiento")
illusion.aprender_hechizo("Invisibilidad")
illusion.aprender_hechizo("Sombra")
illusion.aprender_hechizo("Espejismo")
illusion.aprender_hechizo("Confusión")  # No debería poder
print(f"Hechizos conocidos por {illusion.nombre}: {illusion.hechizos}")
print(illusion.crear_ilusion("Doble fantasma"))

print("\n===INVOCADOR===")
invocador = Invocador("Summon", 80, 60)
dragon_fafnir = Dragon("Fafnir", 300, 200, 80, "fuego")
quimera_threx = Quimera("Threx", 180, 150, 75, ["Veneno", "Fuego", "Electricidad"])
print(invocador.invocar_criatura(dragon_fafnir))
print(invocador.invocar_criatura(quimera_threx))
print("🧬 Criaturas invocadas:")
for criatura in invocador.criaturas_invocables:
    print(f"- {criatura}")  # Esto llama a __str__()


print("\n===DRAGÓN===")
dragon = Dragon("Fafnir", 300, 200, 80, "fuego")
print(f"{dragon.nombre} tiene resistencia a: {dragon.resistencia_elemental}")
print(dragon.escupir_fuego())
print(dragon.ataque_magico())

print("\n===QUIMERA===")
quimera = Quimera("Chimera", 120, 160, 90, ["Rayo", "Hielo", "Veneno"])
print(f"Habilidades por cabeza: {quimera.cabezas}")
print(quimera.usar_habilidad(0))
print(quimera.usar_habilidad(2))
print(quimera.usar_habilidad(3))  # Inválido

print("\n===ESPÍRITU ERRANTE===")
espiritu = EspirituErrante("Fantasma", 500, 50, "aire", 10)
print(f"Afinidad: {espiritu.afinidad_elemental}")
print(espiritu.poseer("Guerrero"))