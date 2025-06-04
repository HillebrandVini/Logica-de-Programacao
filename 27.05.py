# x = 10
# y = 20

# print(f"Soma: {x + y}")
# print(f"Subtração: {x - y}")  
# print(f"Multiplicação: {x * y}")
# print(f"Divisão: {x / y}")

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# if num1 > num2:
#     print(f"O maior número é: {num1}")
# elif num2 > num1:
#     print(f"O maior número é: {num2}")
# else:
#     print("Os números são iguais")

# print(f"Multiplicação: {num1 * num2}")
# print(f"Divisão: {num1 / num2}")
# print(f"Módulo: {num1 % num2}")

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))
# nota3 = float(input("Digite a terceira nota: "))
# nota4 = float(input("Digite a quarta nota: "))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# if media >= 7:
#     print(f"Aprovado com média {media}")
# else:
#     print(f"Reprovado com média {media}")

# pares = []
# impares = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

# print(f"Números pares: {pares}")
# print(f"Números ímpares: {impares}")

# num = int(input("Digite um número de 1 a 10: "))
# for i in range(1, 11):
#     print(num * i)

# numeros = []
# maiores = []
# contador = 0
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# num4 = int(input("Digite o quarto número: "))
# num5 = int(input("Digite o quinto número: "))

# numeros.append(num1)
# numeros.append(num2)
# numeros.append(num3)
# numeros.append(num4)
# numeros.append(num5)

# for i in range(len(numeros)):
#     if i > 10:
#         maiores.append(i)
#         contador += 1

# print(f"Números maiores que 10: {maiores}")
# print(f"Quantidade de números maiores que 10: {contador}")

# idade = int(input("Digite sua idade: "))
# carteira = input("Você tem carteira de motorista? (s/n): ")

# if idade >= 18 and carteira == "s":
#     print("Você pode dirigir")
# else:
#     print("Você não pode dirigir")

# nota1 = float(input("Digite a primeira nota: "))
# nota2 = float(input("Digite a segunda nota: "))

# if nota1 > 7 or nota2 > 7 or nota1 + nota2 > 12:
#     print("Aprovado")


# lista = []
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))
# num4 = int(input("Digite o quarto número: "))
# num5 = int(input("Digite o quinto número: "))

# lista.append(num1)
# lista.append(num2)
# lista.append(num3)
# lista.append(num4)
# lista.append(num5)

# lista.sort()
# media = sum(lista) / len(lista)
# print(lista[0])
# print(lista[-1])
# print(media)
    

# nome = ['Juliana', 'Pedro', 'Maria', 'João']
# idade = [15, 18, 25, 10]

# for i in range(4):
#     if idade[i] >= 18:
#         print(f'{nome[i]} é maior de idade')


# def soma(a, b):
#     return a + b

# def media(lista):
#     return sum(lista) / len(lista)

# def primo(n):
#     for i in range(1, n):
#         if n % i == 0:
#             if i != n and i != 1:
#                 print(f'{n} não é primo')
#                 break
#     else:
#         print(f'{n} é primo')

# primo(11)

# def nomes(lista):
#     contador = 0
#     for i in range(len(lista)):
#         contador = 0
#         for j in lista[i]:
#             contador += 1
#             if contador > 5:
#                 print(f'{lista[i]} é maior que 5')

# nomes(['João', 'Maria', 'Pedroo', 'Ana'])\
