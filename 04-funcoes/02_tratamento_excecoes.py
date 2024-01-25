def divisao(a, b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("Erro: impossívem dividir uma valor por zero")
    except TypeError as e:
        print(f'Erro: o tipo de dado informado está incorreto. \n Detalhes: {e}')
    else:
        print('Sem excecoes')

divisao(10,'hj')