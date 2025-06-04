nota1 = float(input("INSIRA A PRIMEIRA NOTA: "))
nota2 = float(input("INSIRA A SEGUNDA NOTA: "))
nota3 = float(input("INSIRA A TERCEIRA NOTA: "))

media = (nota1 + nota2 + nota3)/2

if media >= 7:
    print(f"APROVADO COM A MEDIA DE: {media:.2f}")
elif media >= 5 < 7:
    print(f"RECUPERAÇÃO COM A MEDIA DE: {media:.2f}")
else:
    print(f"REPROVADO COM A MEDIA DE: {media:.2f}")