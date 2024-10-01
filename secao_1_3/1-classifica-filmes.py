print('Bem-Vindo a máquina de vendas automática de ingressos de cinema!')

idade = int(input('Por favor, digite sua idade: \n'))

filmes = [
    {
        'title': 'Filme 1',
        'description': 'Descrição 1',
        'classificacao': 'Não Preenchido',
    },
    {
        'title': 'Filme 2',
        'description': 'Descrição 2',
        'classificacao': 'Não Preenchido',
    },
    {
        'title': 'Filme 3',
        'description': 'Descrição 3',
        'classificacao': 'Não Preenchido',
    },
    {
        'title': 'Filme 4',
        'description': 'Descrição 4',
        'classificacao': 'Não Preenchido',
    },
    {
        'title': 'Filme 5',
        'description': 'Descrição 5',
        'classificacao': 'Não Preenchido',
    },
]

for index, filme in enumerate(filmes):
    while True:
        classificacao = int(input(f'{filme['title']} de 1 a 5? (0 para parar): '))
        if classificacao <= 0:
            print(f'Pulando o filme "{filme['title']}"\n')
            break
        elif classificacao > 5:
            print('Classificação inválida! Insira novamente! \n')
        else:
            print(f'{filme['title']} com {classificacao} estrelas. \n')
            filmes[index]['classificacao'] = classificacao
            break
else:
    print(filmes)