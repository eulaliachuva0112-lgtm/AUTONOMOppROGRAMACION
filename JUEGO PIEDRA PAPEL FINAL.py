import random

opciones = ["piedra", "papel", "tijera"]

while True:
    print("\n=== Juego Piedra, Papel o Tijera ===")
    usuario = input("Elige piedra, papel o tijera (o 'salir'): ").lower()

    if usuario == "salir":
        print("Fin del juego")
        break

    if usuario not in opciones:
        print("Opcion no valida. Intenta de nuevo.")
        continue

    sistema = random.choice(opciones)
    print("La computadora eligio:", sistema)

    if usuario == sistema:
        print("Resultado: Empate")
    elif (usuario == "piedra" and sistema == "tijera") or \
         (usuario == "papel" and sistema == "piedra") or \
         (usuario == "tijera" and sistema == "papel"):
        print("Resultado: Ganaste")
    else:
        print("Resultado: Perdiste")

    repetir = input("Quieres volver a intentarlo? (si/no): ").lower()
    if repetir != "si":
        print("Fin del juego")
        print("Gracias por jugar")
        break