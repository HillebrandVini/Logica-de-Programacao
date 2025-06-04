# armazena a resposta em variaveis
x = input("Digite um numero inteiro: ")
y = input("Digite mais um numero inteiro: ")
# transforma string em int
x = int(x)
y = int(y)
# faz o calculo
d = (x ** 2) - (y ** 3)
# aplica o modulo
if (d < 0):
    d *= -1
# printa
print(d)