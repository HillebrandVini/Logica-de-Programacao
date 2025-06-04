# armazena os valores nas varaveis
c = input("Digite o capital inicial: ")
r = input("Digite a taxa de juros compostos: ")
t = input("Digite por quanto meses: ")
# transforma em float/int
c = float(c)
r = float(r)
t = int(t)
# faz o calculo
m = c * ((1 + r/100) ** t)
# faz uma diferença que se denomina como lucro
lucro = m - c
# printa
print("Seu lucro foi de: ", round(lucro, 2),"Esse foi o valor final: ", round(m, 2))