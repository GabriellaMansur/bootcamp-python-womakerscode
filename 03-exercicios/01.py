perguntas = ['Telefonou para a vítima? (S / N): ','Esteve no local do crime: (S / N) ', 'Mora perto da vítima?: (S / N) ', 'Devia para a vítima?: (S / N) ', 'Já trabalhou a vítima?:  (S / N)' ]

respostaPositiva = []
    
for pergunta in perguntas:
    resposta = input(pergunta + ' ').upper()
    if resposta == 'S':
        respostaPositiva.append(resposta)


if len(respostaPositiva) == 2:
    print('Suspeita')
elif len(respostaPositiva) == 3 or len(respostaPositiva) == 4:
    print('Cúmplice')
elif len(respostaPositiva) == 5:
    print('Assasino')
else:
    print('Inocente')
