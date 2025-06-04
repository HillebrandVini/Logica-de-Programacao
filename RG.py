import random

# rg = []
# lista = []
# cal = 0
# cont = 0

# for i in range(8):
#     rg.append(random.randint( 0, 9))
#     if rg[i] < 5:
#         cal = rg[i] - 5
#         cal = cal * -1
#         cont = rg[i] * cal
#     elif rg[i] == 5:
#         cal = rg[i] - 7
#         cal = cal * -1
#         cont = rg[i] * cal
#     elif rg[i] > 5 < 9:
#         cal = rg[i] - 10
#         cal = cal * -1
#         cont = rg[i] * cal
#     lista.append(cont)


# result = 0

# result = sum(lista)
# result = result % 11
# result = 11 - result

# cv1 = result
# rg.append(cv1)

# lista.clear()

# for i in range(8):
#     if rg[i] < 5:
#         cal = rg[i] - 5
#         cal = cal * -1
#         cont = rg[i] * cal
#     elif rg[i] == 5:
#         cal = rg[i] - 7
#         cal = cal * -1
#         cont = rg[i] * cal
#     elif rg[i] > 5 < 9:
#         cal = rg[i] - 10
#         cal = cal * -1
#         cont = rg[i] * cal
#     lista.append(cont)
    
# result = 0

# result = sum(lista)
# result = result % 11
# result = 11 - result

# cv1 = result
# rg.append(cv1)
# print(rg)


rg = input("Primeiros 8 digitos do RG:")
listarg = []
cal = 0
cont = 0

for i in range(8):
    listarg.append(rg[i])
    listarg[i] = int(listarg[i])

lista = []

for i in range(8):
    if listarg[i] == 2:
        cal = 2
        cont = listarg[i] * cal
    elif listarg[i] == 1:
        cal = listarg[i] - 4
        cal = cal * -1
        cont = listarg[i] * cal
    elif listarg[i] > 2 < 10:
        cal = listarg[i] - 10
        cal = cal * -1
        cont = listarg[i] * cal
    lista.append(cont)
print(lista)
result = 0

result = sum(lista)
print(result)
result = result % 11
print(result)
result = 11 - result
cv1 = result
listarg.append(cv1)
print(listarg)
