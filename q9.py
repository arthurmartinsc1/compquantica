import math
import numpy as np

def cis(theta):
    return complex(math.cos(2 * np.pi * theta), math.sin(2 * np.pi * theta))

str1 = input("Digite o número complexo que deseja transformar no formato a+bj: ")
c1 = complex(str1)

theta1 = (math.acos(c1.real/abs(c1)))

print(" o novo complexo tem modulo e angulo em radiano definidos como ",abs(c1),theta1)




