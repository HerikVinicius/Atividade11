print("Calculador do preço da passagem")
dist = float(input("Digite a distância da viagem em Km: "))
if dist<=200:
    print(f"O valor da passagem é de {dist*0.50}")
else:
    print(f"O valor da passagem é de {dist*0.45}")