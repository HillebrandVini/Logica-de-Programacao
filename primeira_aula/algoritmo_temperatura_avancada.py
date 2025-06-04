# pega o string digitado e armazena na variavel celsius
celsius = input("Digite uma temperatura em graus celsius")
# transforma o string em float
celsius = float(celsius)
# 6 a 8 faz as conversoes 
kelvin = celsius + 273.15
fahrenheit = (9/5 * celsius) + 32
rankine = kelvin * 9/5

# printa os resultados com duas casas decimais
print("Celsius: ", round(celsius, 2))
print("Kelvin: ", round(kelvin,2))
print("Fahrenheit: ", round(fahrenheit, 2))
print("Rankine: ", round(rankine, 2))