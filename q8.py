import matplotlib.pyplot as plt
import numpy as np

# Defina números complexos

z1 = 2 -1j
z2 = 1+1j

z3=z1+z2
z4 = z1-z2
numeros_complexos = [z1,z2,z3,z4]


partes_reais = [num.real for num in numeros_complexos]
partes_imaginarias = [num.imag for num in numeros_complexos]






plt.figure(figsize=(8,8))
plt.scatter(partes_reais, partes_imaginarias, color='red')


for i, txt in enumerate(numeros_complexos):
    plt.annotate(txt, (partes_reais[i], partes_imaginarias[i]), fontsize=8)
    
    
for num in numeros_complexos:
    plt.quiver(0, 0, num.real, num.imag, angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.5)





plt.title('Plano Complexo')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.grid()
# Exiba o gráfico
plt.show()



#item b incluso



