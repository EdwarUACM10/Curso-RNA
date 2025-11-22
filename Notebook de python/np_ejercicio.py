
import numpy as np
class McCullochPittsNeuron:
    def __init__(self, threshold):
        """
        Inicializa la neurona con un umbral.
        :param threshold: Umbral para la función de activación
        """
        self.threshold = threshold

    def activate(self, inputs):
        """
        Calcula la salida de la neurona basada en las entradas.
        :param inputs: Lista o array de entradas (0 o 1)
        :return: Salida de la neurona (0 o 1)
        """
        # Calcula la suma de las entradas
        print(inputs)
        weighted_sum = inputs.sum() # suma todos los elementos
        
        # Aplica la función de activación (umbral)
        activacion = 0 
        if weighted_sum >= self.threshold: 
            activacion = 1
        return activacion

# Configura el umbral para la función AND

threshold = 2  # Umbral para que la suma sea al menos 2 para producir salida 1

# Crea la neurona
neuron = McCullochPittsNeuron(threshold)

# Prueba la neurona con todas las combinaciones de entradas para la función AND
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Imprime las salidas para cada combinación de entradas
for inp in inputs:
    output = neuron.activate(inp)
    print(f"Entrada: {inp}, Salida: {output}")