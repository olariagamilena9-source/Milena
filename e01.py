nom = 0
edad = 0
añodenacimiento = 0
añoactual = 0

nombre = input("¿Cual es tu nombre?")

print("Hola", nombre)
añodenacimiento = int(input("¿En que año naciste?"))
añoactual  = int(input("¿En que año estamos?"))

edad = añoactual - añodenacimiento

print("Tu edad es:", edad)