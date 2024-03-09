
str1 = input("digite um numero complexo da forma a+bj")
str2 = input("digite um numero complexo da forma a+bj")
str3 = input("digite um numero complexo da forma a+bj")
str4 = input("digite um numero complexo da forma a+bj")

a = complex(str1)
b = complex(str2)
c = complex(str3)
d = complex(str4)



if a*d - b*c == 0:
    print("nao é possivel realizar a transformada")


str5 = input("digite um numero complexo da forma a+bj")
x = complex(str5)
R = ((a*x) +b/(c*x) +d)


print('o valor da transformada é ',R)
