import random

opciones = ["piedra", "papel", "tijera"]

print("=== Juego Piedra, Papel o Tijera ===")
usuario = input("Elige una opción: piedra, papel o tijera: ").lower()

if usuario not in opciones:
    print("Opción no válida")
else:
    sistema = random.choice(opciones)
    print("La computadora eligió:", sistema)

    if usuario == sistema:
        print("¡Empate!")
    elif (usuario == "piedra" and sistema == "tijera") or \
         (usuario == "papel" and sistema == "piedra") or \
         (usuario == "tijera" and sistema == "papel"):
        print("¡Ganaste!")
    else:
        print("Perdiste :(")
