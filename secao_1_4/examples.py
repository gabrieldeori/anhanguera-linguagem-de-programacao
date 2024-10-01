print('Imprime o comprimento da lista')
numeros = [1, 2, 3, 4, 5]

print('Usa a função len() para calcular o comprimento da lista')
COMPRIMENTO = len(numeros)
print(COMPRIMENTO)

print('Função Soma:')
# Definindo uma função chamada "soma"


def soma(a, b):
    resultado = a + b
    return resultado


# Chamando a função e armazenando o resultado em uma variável
RESULTADO = soma(5, 3)

# Imprimindo o resultado
print(RESULTADO)

print('Definindo uma função chamada "e_par"')


def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


print('Testando a função')
NUMERO = 123120

if e_par(NUMERO):

    print(f'{NUMERO} é um número par.')

else:

    print(f'{NUMERO} não é um número par.')

print('Função lambda:')
SOMA = lambda a, b: a + b
RESULTADO = SOMA(3, 4)
print(RESULTADO)
