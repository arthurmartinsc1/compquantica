import numpy as np
def verificar_unitaria(matriz):
    matriz_conjugada_transposta = matriz.conj().T
    return np.allclose(np.dot(matriz, matriz_conjugada_transposta), np.eye(matriz.shape[0]))
n_linhas = int(input("Digite o número de linhas da matriz: "))
n_colunas = int(input("Digite o número de colunas da matriz: "))
matriz = np.array([[complex(input(f"Digite o elemento ({i+1},{j+1}) da matriz (formato a+bj): ")) for j in range(n_colunas)] for i in range(n_linhas)])
if matriz.shape[0] != matriz.shape[1]:
    print("A matriz não é quadrada e, portanto, não pode ser unitária.")
else:
    if verificar_unitaria(matriz):
        print("A matriz é unitária.")
    else:
        print("A matriz não é unitária.")