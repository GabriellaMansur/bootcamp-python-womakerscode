salarioBruto = float(input('Digite o seu salário bruto: '))

if salarioBruto <= 1903.98:
    salarioLiquido = salarioBruto
elif salarioBruto > 1903.99 and salarioBruto < 2826.65:
    salarioLiquido = salarioBruto - (salarioBruto * 0.075)
elif salarioBruto > 2826.65 and salarioBruto <= 3751.05:
   salarioLiquido = salarioBruto - (salarioBruto * 0.15)
elif salarioBruto > 3751.05 and salarioBruto <= 4664.68:
    salarioLiquido = salarioBruto - (salarioBruto * 0.225)
else:
   salarioLiquido = salarioBruto - (salarioBruto * 0.275)

print(f'Seu salário líquido é R$ {salarioLiquido:.2f}')