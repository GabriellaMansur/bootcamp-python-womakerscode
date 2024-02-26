numeros = []

for _ in range(3):
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            print('Apenas números positivos são válidos')
        else:
            numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

num_ordenados = sorted(numeros)

print("Números digitados:", num_ordenados)