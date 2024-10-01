# Operações
# x in s
# True caso um item de s seja igual a x, senão false.
# s + t
# Concatenação de s e t.
# n * s
# Adiciona s a si mesmo n vezes.
# s[i]
# Acessa o valor guardado na posição i da sequência.
# s[i:j]
# Acessa os valores da posição i até j.
# s[i:j:k]
# Acessa os valores da posição i até j, com passo k.
# len(s)
# Comprimento de s.
# min(s)
# Menor valor de s.
# max(s)
# Maior valor de s.
# s.count(x)
# Número total de ocorrência de x em s.

print('Objetos tipo sequência:')
TEXTO = 'Explorando a diversidade de linguagens de programação com Pyhton.'

print(f'Tamanho do TEXTO = {len(TEXTO)}')
print(f'Python in TEXTO = {'Python' in TEXTO}')
print(f'Quantidade de e no TEXTO = {TEXTO.count('e')}')
print(f'As 5 primeiras letras são: {TEXTO[:5]}')


print('Listas:')
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
for cor in cores:
    print(f'Posição = {cores.index(cor)}, cor = {cor}')

print('\n\n')

linguagens = [
    'Python', 'Java', 'JavaScript', 'C', 'C#', 'C++', 'Swift', 'Go', 'Kotlin'
]
print('Antes da listcomp = ', linguagens)
print('\n')
linguagens = [item.lower() for item in linguagens]
print('\nDepois da listcomp = ', linguagens)

print('\n\n')
print('lambda e map:')
precos_em_dolares = [100, 50, 75, 120]
TAXA_CAMBIO = 5.25
precos_em_reais = list(map(lambda x: x * TAXA_CAMBIO, precos_em_dolares))
print(precos_em_reais)

print('\n\n')
print('Filter ex. pares:')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)

print('\n\n')
print('Tuplas e enumerate:')
vogais = ('a', 'e', 'i', 'o', 'u')

print(f'Tipo do objeto vogais = {type(vogais)}')
for p, x in enumerate(vogais):
    print(f'Posição = {p}, valor = {x}')

