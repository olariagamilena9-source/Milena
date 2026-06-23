suma = 0
mult = 1
M = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

for i in range(4):
    for j in range(4):
        if(i==j):
            suma = suma+M[i][j]
            mult = mult*M[i][j]
            
print("La suma es", suma)
print("La multiplicación es", mult)