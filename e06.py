monto = 0
billetes1000 = 0
billetes200 = 0
resto = 0
restofinal = 0

monto = int(input("¿Cuanto dinero queres extraer?:"))

billetes1000 = (monto/1000)
resto = (resto%200)

print("Billetes de $1000", billetes1000)
print("Billetes de $200", billetes200)
print("Dinero no entregado", restofinal)