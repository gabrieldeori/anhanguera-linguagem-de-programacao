# Você está gerenciando a lista de convidados de uma festa e a lista de
# pessoas que confirmaram a presença no evento. Você deseja identificar
# as pessoas que ainda não confirmaram presença, a fim de convidá-las
# novamente.

convidados = ('Alice', 'Bob', 'Carol', 'David', 'Eve')
confirmados = ('Eve', 'Carol')

nao_confirmados = [
    convidado for convidado in convidados if convidado not in confirmados
]

print('Convidados que ainda não confirmaram: ')
for pessoa in nao_confirmados:
    print(pessoa)
