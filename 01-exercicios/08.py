valor_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))

salario_mes = valor_hora * horas_trabalhadas

print(f"O seu salário do mês referido é de R$ {salario_mes:.2f}")