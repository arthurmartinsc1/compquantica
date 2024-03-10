
n = int(input("digite a dimensao da matriz quadrada: "))
def transposta(matriz):
    
    result = []
    
    for i in range(len(matriz)):
        linharesult=[]
        for j in range(len(matriz[0])):
            elemento = matriz[j][i]
            linharesult.append(elemento)
            
            
        result.append(linharesult)
        
        
    return result    
def matrizconjug(matriz):
    result = []
    
    for i in range(len(matriz)):
        linharesult = []
        for j in range(len(matriz[0])):
            elementos = ((matriz[i][j]).conjugate())
            linharesult.append(elementos)
            
        result.append(linharesult)
        
    return result     
def recebermatriz():
    
    linhas = n
    colunas = n
    Matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            elementos = complex(input("digite um complexo da forma a+bj: "))
            linha.append(elementos)
  
        Matriz.append(linha)
    
    return Matriz
def prodint(matriz1,matriz2):
    
    
    result = 0
    
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            result += matriz1[i][j] * matriz2[i][j]
            
    return result       


matriz1 = recebermatriz()
matriz2 = matrizconjug(matriz1)
matriz3 = transposta(matriz1)


n1 = prodint(matriz1,matriz2)
n2 = prodint(matriz1,matriz3)

if n1 == n2:
    print("matrizes sao hermitianas")
    
else:
    print("matrizes nao hermitianas")   
