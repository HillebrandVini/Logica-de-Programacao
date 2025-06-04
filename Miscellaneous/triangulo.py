a = float(input("digite o numero do primeiro lado: "))
b = float(input("digite o numero do segundo lado: "))
c = float(input("digite o numero do ultimo lado: "))

if a == b == c:
    print("Seu triângulo é Equilátero")
elif a != b and a != c and b != c:
    print("Seu triângulo é Escaleno")
elif a == b != c or a == c != b or c == b != a:
    print("Seu triângulo é Isóceles")