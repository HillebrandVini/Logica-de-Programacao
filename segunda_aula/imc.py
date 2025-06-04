peso = float(input("Insira seu peso em kg: "))
altura = float(input("Insira sua altura em metros:"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Voce esta abaixo do peso: {imc:.2f}")
elif imc >= 18.5 < 25:
    print(f"Voce esta no peso ideal: {imc:.2f}")
elif imc >= 25 < 30:
    print(f"Voce esta acima do peso: {imc:.2f}")
else:
    print(f"Voce esta obeso: {imc:.2f}")