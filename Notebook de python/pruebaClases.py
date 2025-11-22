class Modelo_Ia:
    def __init__(self, nombre_modelo):
        self.nombre_modelo =  nombre_modelo

    def entrenar(self,datos,etiquetas):
        modelo = self.nombre_modelo
        print("Entrenando el modelo: {} con datos:{} y etiquetas: {}".format(modelo,datos,etiquetas))
    def predecir(self,datos):
        print("Prediccion con los siguientes datos:", datos)
    
class Modelo_SVM(Modelo_Ia):
    def __init__(self,parametro_regulacion, C=1.0):
        super().__init__("Modelo_SVM")
        self.parametro_regulacion= parametro_regulacion
        self.C=C

    def entrenar(self, datos, etiquetas):
        super().entrenar(datos, etiquetas)
        print(f"con parametros de regulacion: {self.parametro_regulacion} C={self.C}")


class Modelo_Nearest_Neighbors(Modelo_Ia):
    def __init__(self,k,numero_vecinos):
        super().__init__("Modelo_NearestNeighbors")
        self.k=k
        self.numero_vecinos=numero_vecinos
        
    def entrenar(self, datos, etiquetas):
        super().entrenar(datos, etiquetas)
        print(f"con numero de vecinos: {self.numero_vecinos} K={self.k}")

class Modelo_Red_Neuronal(Modelo_Ia):
    def __init__(self, capas_ocultas,numero_neuronas,salidas):
        super().__init__("Modelo_RedNeuronal")
        self.capas_ocultas=capas_ocultas
        self.numero_neuronas=numero_neuronas
        self.salidas=salidas
    def entrenar(self, datos, etiquetas):
        super().entrenar(datos, etiquetas) 
        print(f"con capas ocultas: {self.capas_ocultas}, numero de neuronas {self.numero_neuronas}  y {self.salidas} salidas")

#  Simulación
# Datos de ejemplo
datos_ejemplo = [[1,2,3],[4,5,6],[7,8,9]]
etiquetas_ejemplo = ["A","B","C"]

# Instanciación de modelos
svm = Modelo_SVM(0.1,C=1.0)
knn = Modelo_Nearest_Neighbors(3,5)
rna = Modelo_Red_Neuronal(1,10,2)

# Entrenamiento
svm.entrenar( datos_ejemplo,etiquetas_ejemplo)
#Predccion
svm.predecir(datos_ejemplo)

knn.entrenar(datos_ejemplo, etiquetas_ejemplo)
knn.predecir(datos_ejemplo)
rna.entrenar(datos_ejemplo, etiquetas_ejemplo)
rna.predecir(datos_ejemplo)

