caramelos = 0
porestudiante = 0
sobran = 0
estudiantes = 0

caramelos = int(input("Ingrese la cantidad de caramelos:"))
estudiantes = int(input("Ingrese la cantidad de estudiantes:"))

porestudiante = (caramelos/estudiantes)
sobran = (caramelos%estudiantes)

print("A cada estudiante le toca:", porestudiante)
print("Sobran:", sobran)