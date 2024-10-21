

import random

numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 5
adivinado = False


print("BIENVENIDO AL JUEGO DE ADIVINANZA DEL NÚMERO OCULTO")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("INTRODUCE UN NÚMERO DEL 1 AL 99: ")
    numero = int(entrada)
    if numero == numero_secreto:
        print("¡FELICITACIONES! USTED A ADIVINADO EL NÚMERO SECRETO")
        adivinado = True
    elif numero < numero_secreto:
        print("EL NÚMERO ES MAYOR AL INGRESADO")
    else:
        print("EL NÚMERO ES MENOR AL INGRESADO")
    cant_intentos += 1
if not cant_intentos < cant_max_intentos:
    print("GAME OVER... NO HAS PODIDO ADIVINAR EL NÚMERO")
       
