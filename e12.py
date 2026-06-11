import random

estudiantes = ['Valen', 'Mia', 'Damon', 'Elena', 'Rebekah']

orden = []
usados = []

for i in range(len(estudiantes)):
    pos = random.randint(0, len(estudiantes) - 1)
    
    while pos in usados:
        pos = random.randint(0, len(estudiantes) - 1)
        
    usados.append(pos)
    orden.append(estudiantes[pos])
        
print("Orden para exponer:")
for i in range(len(orden)):
    print(i + 1, "-", orden[i])