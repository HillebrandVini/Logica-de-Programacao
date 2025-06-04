# importa a biblioteca de matematica do python
import math
# armazena os valores e coverte pra float
raio = input("Informe o raio: ")
raio = float(raio)
altura = input("Informe a altura: ")
altura = float(altura)
# calcula a area
area = math.pi * (raio ** 2)
# calcula o volume
volume = area * altura
# printa
print(volume)