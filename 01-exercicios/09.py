horas_exercicios_semana = float(input("Digite  número de horas de exercício por semana: "))

calorias_perdidas_minuto = 5
semanas_mes = 4

calorias_perdidas_mes = (horas_exercicios_semana * 60) * calorias_perdidas_minuto * semanas_mes

print(f"A quantidade de calorias perdidas no mês foi {calorias_perdidas_mes}")