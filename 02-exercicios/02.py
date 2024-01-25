
turno = input("Digite qual turno você estuda. (Opções: M- matutino, V- vespertino, N- noturno) ").upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde')
elif turno =='N':
    print('Boa noite')
else: 
    print('Valor inválido')
