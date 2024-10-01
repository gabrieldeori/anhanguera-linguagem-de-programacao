print('Repetição em listas:')
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)

print('While')
numero = int(input())

while numero != 0:
    if numero % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    numero = int(
        input(
            'Insira valor para saber par ou ímpar e 0 pra sair!'
        )
    )

print('Range')
for x in range(5):
    print(x)

print('Range com limite inferior e superior:')
for y in range(2, 7):
    print(y)

print('Range com limite e incremento:')
for z in range(1, 11, 2):
    print(z)

print('Ex uso do break (Primeiro par):')
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
        break

print('Ex. continue como exceção a valor 5:')
for numero in range(1, 11):
    if numero == 5:
        continue

    print(numero)
