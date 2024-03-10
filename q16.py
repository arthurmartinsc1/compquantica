import cmath

n = int(input("digite o valor da dimensao da matrzi quadrada"))


def recebermatriz():
    
    linhas = n
    colunas = n
    Matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elementos = complex(input("digite um complexo da forma a+bj"))
            linha.append(elementos)
  
        Matriz.append(linha)
    
    return Matriz  

    
  

matriz1 = recebermatriz()

def transposta(matriz):
    
    result = []
    
    for i in range(len(matriz)):
        linharesult=[]
        for j in range(len(matriz[0])):
            elemento = matriz[j][i]
            linharesult.append(elemento)
            
            
        result.append(linharesult)
        
        
    return result    


matriztransp = transposta(matriz1)


for linhas in matriztransp:
    print(linhas)
    
    
    
def matrizconjug(matriz):
    result = []
    
    for i in range(len(matriz)):
        linharesult = []
        for j in range(len(matriz[0])):
            elementos = ((matriz[i][j]).conjugate())
            linharesult.append(elementos)
            
        result.append(linharesult)
        
    return result     
    


matrizconjugate = matrizconjug(matriz1)
for linhas in matrizconjugate:
    print(linhas)
    



