p = 1j*1j

q = p*1j

r = q*1j

t = r*1j

#iremos imprimir agora o valor de t e constatar que eh igual a 



#dessa forma, vemos que pow(i,3)= pow(i,7)= pow(i,11)= pow(i,15)


#assim temos que: 
n = int(input("digite o valor de n"))


if(n%4 == 0):
    
    print(" ",r)
    
if(n%4 ==1):
    print(" ",1j)  
    
if(n%4 ==2):
    
    print(" ",p)   


if(n%4 == 3):
    
    print("",q)