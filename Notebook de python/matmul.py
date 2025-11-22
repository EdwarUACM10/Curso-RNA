
# primero debo de verificar que el numero de columnas de A sean las mismo numero de filas de B
# Ya que combprobamos eso, entonces nos va a quedar una matriz de C de: m x p 
def multiplicar_matrices(A, B):
    # Verificar si se pueden multiplicar
    if len(A[0]) != len(B):
        print("Error: Las columnas de A deben ser iguales a las filas de B.")
        return None

    # Crear matriz resultado llena de ceros
    C = []
    for i in range(len(A)):  # Recorrer filas de A
        nueva_fila = []
        for j in range(len(B[0])):  # Recorrer columnas de B
            suma = 0
            for k in range(len(B)):  # Recorrer elementos para multiplicar y sumar
                suma += A[i][k] * B[k][j]
                #print(suma)
            nueva_fila.append(suma)
        C.append(nueva_fila)
    
    return C

# Matrices 7+
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

"""
print((B[0][1]))
print(len(A[0]))
print(len(A[1]))
print(len(B[0]))
print(len(B[1]))
print(len(B[2]))
print(len(B))
print(len(A))
"""
print("A:",A)
print("B:",B)
print("Resultado A x B:")

resultado = multiplicar_matrices(A, B)
for fila in resultado:
    print(fila)

