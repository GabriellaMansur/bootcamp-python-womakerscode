resposta = int(input('Digite sua opção: \n Opção 1: converter de Celsius para Fahrenheit. \n Opção 2: converter de Fahrenheit para Celsius \n'))


def converterCelsius(celsius):
    fahrenheit_convertido = celsius * 1.8 + 32
    print(f'O resultado é {fahrenheit_convertido:.2f}° F')


def converterFahrenheit(fahrenheit):
    celsius_convertido = (fahrenheit - 32) / 1.8
    print(f'O resultado é {celsius_convertido:.2f}° C')


if resposta == 1:
    celsius = float(input('Digite os graus celsius a serem convertidos: '))
    converterCelsius(celsius)
elif resposta == 2:
    fahrenheit = float(input('Digite os graus fahrenheit a serem convertidos: '))
    converterFahrenheit(fahrenheit)
else:
    print('Opção inválida. Tente novamente')


# Código melhorado com validações --> estudar e treinar
def converterCelsius(celsius):
    fahrenheit_convertido = celsius * 1.8 + 32
    print(f'O resultado é {fahrenheit_convertido:.2f}° F')


def converterFahrenheit(fahrenheit):
    celsius_convertido = (fahrenheit - 32) / 1.8
    print(f'O resultado é {celsius_convertido:.2f}° C')


while True:
    try:
        resposta = int(input('Digite sua opção: \n Opção 1: converter de Celsius para Fahrenheit. \n Opção 2: converter de Fahrenheit para Celsius \n'))
        if resposta not in (1, 2):
            raise ValueError
        break
    except ValueError:
        print("Opção inválida. Tente novamente.")

if resposta == 1:
    while True:
        try:
            celsius = float(input('Digite os graus celsius a serem convertidos: '))
            break
        except ValueError:
            print("Valor inválido. Tente novamente.")
    converterCelsius(celsius)
else:
    while True:
        try:
            fahrenheit = float(input('Digite os graus fahrenheit a serem convertidos: '))
            break
        except ValueError:
            print("Valor inválido. Tente novamente.")
    converterFahrenheit(fahrenheit)