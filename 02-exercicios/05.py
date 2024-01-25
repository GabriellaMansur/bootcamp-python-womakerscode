print('Esse programa verifica se um triângulo é equilátero, isósceles ou escaleno ')
lado1 = int(input('Digite o primeiro lado : '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digite o terceiro lado : '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print('Não é um triângulo')
elif lado1 == lado2 and lado1 == lado3:
    print('Triângulo equilátero, todos os lados são iguais')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Triângulo isósceles, dois lados são iguais')
else:
    print('Triângulo escaleno, todos os lados são diferentes')
