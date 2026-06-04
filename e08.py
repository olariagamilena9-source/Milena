import math
radio = 0


def area_circulo(radio):
    area = math.pi * radio * radio
    return area

print("Calculadora de radio del circulo")
radio = int(input("Ingrese el radio del circulo"))

def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)
    return area_base * altura

r = float(input("Ingrese el radio: "))
h = float(input("Ingrese la altura: "))

print("Área del círculo:", area_circulo(r))
print("Volumen del cilindro:", volumen_cilindro(r, h))
