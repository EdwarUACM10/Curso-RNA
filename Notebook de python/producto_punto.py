#Primero de verifica que tengan la misma longitud 
#Depues se inicia una varuable que almacenara el resultado 
#y por ultimo iniciamos a multpilicar elementos de indice igual de cada uno de los vectores
#y los guardamos en la variable que almacena el resultado y por ultimo retorna el 
#recultado que es un numero contante.
def producto_punto(a, b):
    # Comprobar que tengan la misma longitud
    if len(a) != len(b):
        print("Error: Los vectores deben tener la misma longitud.")
        return 
    
    total = 0  
    for i in range(len(a)):
        total = total + (a[i] * b[i])  # Multiplicamos y sumamos al total
    
    return total


v1 = [1, 2, 3]
v2 = [4, 5, 6]
C=[]
C.append(v1)
print(C)
C.append(v2)
print(C)

print("Producto punto:", producto_punto(v1, v2))
