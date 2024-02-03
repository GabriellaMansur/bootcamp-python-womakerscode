peso_kg = float(input("Digite seu peso em kgs: "))
altura_metros = float(input("Digite sua altura em metros: "))

imc = peso_kg / (altura_metros**2)

print(f"O seu IMC é {imc:.2f}")