str1 = input("Digite o primeiro complexo no formato a+bj: ")
str2 = input("Digite o segundo complexo no formato a+bj: ")

c1 = complex(str1)
c2 = complex(str2)

barra = '\u0304'

print("teste a:")
print("conj(c1)+conj(c2) = conj(c1+c2)", (c1.conjugate()+c2.conjugate() == (c1+c2).conjugate()))

print("teste b:")
print("conj(c1)*conj(c2) = conj(c1*c2)", (c1.conjugate()*c2.conjugate() == (c1*c2).conjugate()))