
import numpy as np
import math

n = int(input("digite o tamanho das matrizes"))

    
    
def recebermatriz():
    
   
    linhas = n
    colunas = n
    matriz = []
    
    for i in range(linhas):
        linha = []
        
        for j in range(colunas):
            elemento = complex(input("digite um numero complexo da forma a+bj: "))
            linha.append(elemento)
    
        matriz.append(linha)
    
    return matriz

def somar(matriz1,matriz2):
    
    result = []
    
    for i in range(len(matriz1)):
        linharesult = []
    
        for j in range(len(matriz1[0])):
            
            elemento = matriz1[i][j]+ matriz2[i][j]
            linharesult.append(elemento)
            
            
            
        result.append(linharesult)  
          
    return result        

matriz_usuario1 = recebermatriz()
matriz_usuario2 = recebermatriz()


matrizsoma = somar(matriz_usuario1,matriz_usuario2)

            
for linha in matrizsoma:
    
    print(linha)
    
def multiplicaçao(matriz1,k):
    
    result =[]
    
    for i in range(len(matriz1)):
        
        linharesult = []
        for j in range(len(matriz1[0])):
            elemento = k*matriz1[i][j]
            linharesult.append(elemento)
        
        result.append(linharesult)
        
    return result    

k = int(input("digite um escalar: "))
matrizmultiplicada = multiplicaçao(matriz_usuario1,k)


for linhas in matrizmultiplicada:
    print("a matriz multiplicada eh  ", linhas)
    
    
    


    
    
        
        


    
    
    



