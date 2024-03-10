

n = int(input("digite a dimensao da matriz quadrada: "))

def traço(matriz):
    
    resultado = 0
    
    for i in range(len(matriz)):
        resultado += matriz[i][i]
        
        
    return resultado    

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

n1 = traço(matriz1)

print("o traço eh: ", n1)

            