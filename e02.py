numerosectreto = 0

import random
numerosecreto = random.randint(1,20)

intentos = 6

print("Adivina el numero entre el 1 y 20")
print("Tienes 6 intentos")

for i in range(intentos):
    intentos = int(input("Ingrese un numero:"))
    
    if intentos == numerosectreto:
        print("¡Correcto! Adivinaste el numero")
        
    elif intentos < numerosecreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")
        
else:
    print("Perdiste, el numero era:", numerosecreto)