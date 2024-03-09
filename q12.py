import matplotlib.pyplot as plt
import numpy as np

str1 = input("Digite um número complexo na forma a+bj: ")
z1 = complex(str1)
labels = []
for n in range(1,11):
    
    str1 = ('Z',n)
    labels.append(str1)
resultados = []

for n in range(1, 11):  # Corrigido para iterar até 10
    resultado = z1**n
    resultados.append(resultado)

real_part = [num.real for num in resultados]
imaginary_part = [num.imag for num in resultados]
for label, x, y in zip(labels, real_part, imaginary_part):
        plt.text(x, y, label)
plt.scatter(real_part, imaginary_part, color='red')

plt.xlabel('Parte Real', color='green')  
plt.ylabel('Parte Imaginária', color='green') 

plt.title('Gráfico de Números Complexos')

plt.grid(True)
plt.show()
