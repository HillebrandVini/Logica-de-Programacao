print("aaa");
print("Um conjunto de algoritmos dão origem a que?");
print("Um programa.");
 
# thiago
# isaque
# estevao
# gabriela

nome = input("nome:")
nome = nome.upper()
lista_nome = []
lista_binario = [""]
lista_letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for char in nome:
    if char in lista_letras:
        ascii_value = ord(char)
        lista_nome.append(ascii_value)


for value in lista_nome:
    binary = ""
    while value > 0:
        binary = str(value % 2) + binary
        value = value // 2
    lista_binario.append(binary)

print(lista_nome, lista_binario)