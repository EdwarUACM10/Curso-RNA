import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creamos datos simulados
data1 = np.random.normal(0, 1, 1000)   # μ=0, σ=1
data2 = np.random.normal(5, 2, 1000)   # μ=5, σ=2

# Graficamos
sns.kdeplot(data1, label="μ=0, σ=1")
sns.kdeplot(data2, label="μ=5, σ=2")
plt.legend()
plt.title("Distribuciones normales con diferente media y varianza")
plt.show()

"""
La primera campana está centrada en 0 y es más angosta.
La segunda está centrada en 5 y más ancha (porque la varianza es mayor).
"""