Nota_1 = int(input('Insira a nota 1: '))
Nota_2 = int(input('Insira a nota 2: '))
Nota_3 = int(input('Insira a nota 3: '))
Nota_4 = int(input('Insira a nota 4: '))

QUANTIDADE_NOTAS = 4

soma_total = Nota_1 + Nota_2 + Nota_3 + Nota_4

media = soma_total / QUANTIDADE_NOTAS

print(f'Média: {media}')

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
