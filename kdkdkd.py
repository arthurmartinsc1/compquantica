import matplotlib.pyplot as plt

import numpy as np


labels = ['Z1','Z1 x Ro']
str1 = input("digite um complexo da forma a+bj ")

z1 = complex(str1)
z2 = z1*(z1.real)
print(" ",z2)
complex_numbers = [z1,z2]

real_part = [num.real for num in complex_numbers]
imaginary_part = [num.imag for num in complex_numbers]

for label, x, y in zip(labels, real_part, imaginary_part):
    plt.text(x, y, label)
plt.scatter(real_part,imaginary_part,color = 'blue',)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')


plt.title('Gráfico de Números Complexos')


plt.grid(True)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

