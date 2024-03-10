
n = int(input("digite a dimensao da matriz quadrada: "))

def prodint(matriz1,matriz2):
    
    
    result = 0
    
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            result += matriz1[i][j] * matriz2[i][j]
            
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



matriz1 = recebermatriz()
matriz2 = recebermatriz()
 
 
n1 = prodint(matriz1,matriz2)      

print(n1) 