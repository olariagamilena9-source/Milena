matriz = []
numero = 1

for i in range(4):
    fila = []
    for j in range(4):
        fila.append(numero)
        numero += 1
    matriz.append(fila)

print("Matriz:")
for fila in matriz:
    print(fila)

suma = 0
multiplicacion = 1

for i in range(4):
    suma += matriz[i][i]
    multiplicacion *= matriz[i][i]

print("\nSuma de la diagonal:", suma)
print("Multiplicación de la diagonal:", multiplicacion)