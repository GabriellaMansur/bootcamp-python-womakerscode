notas1 = []
notas2 = []
notas3 = []
medias = []

for i in range(4):
    aluno1 = float(input(f'Aluno 1, digite a nota {i+1}: '))
    notas1.append(aluno1)

media1 = sum(notas1) / len(notas1)
medias.append(media1)

for i in range(4):
    aluno2 = float(input(f'Aluno 2, digite a nota {i+1}: '))
    notas2.append(aluno2)

media2 = sum(notas2) / len(notas2)
medias.append(media2)

for i in range(4):
    aluno3 = float(input(f'Aluno 3, digite a nota {i+1}: '))
    notas3.append(aluno3)

media3 = sum(notas3) / len(notas3)
medias.append(media3)



aprovados = 0

if medias[0] >= 7:
    aprovados += 1
    print("Aluno 1 aprovado")

if medias[1] >= 7:
    print("Aluno 2 aprovado")
    aprovados += 1
    

if medias[2] >= 7:
    print("Aluno 3 aprovado")
    aprovados += 1

# outra forma:

notas = []
for i in range(3):
    aluno = []
    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        aluno.append(nota)
    notas.append(aluno)

medias = []
for aluno in notas:
    media = sum(aluno) / len(aluno)
    medias.append(media)

aprovados = 0
for media in medias:
    if media >= 7:
        aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é {aprovados}.")    
