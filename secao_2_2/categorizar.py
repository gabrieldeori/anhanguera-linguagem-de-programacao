import numpy

participantes = (
    {
        'nome': 'Alice',
        'localizacao': 'EUA',
        'afiliacao': 'Universidade A',
        'interesses': ['Física', 'Astronomia']
    },
    {
        'nome': 'Bob',
        'localizacao': 'Brasil',
        'afiliacao': 'Instituto B',
        'interesses': ['Biologia', 'Astronomia']
    },
    {
        'nome': 'Charlie',
        'localizacao': 'Índia',
        'afiliacao': 'Instituto C',
        'interesses': ['Química', 'Engenharia']
    }
)


regioes = set(participante['localizacao'] for participante in participantes)

afiliacoes = {}

for participante in participantes:
    afiliacao = participante['afiliacao']

    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante['nome'])

# Numpy
areas_de_interesse = numpy.array(
    [
        interesse for participante in participantes
        for interesse in participante['interesses']
    ]
)

interesses_unicos, contagem = numpy.unique(
    areas_de_interesse, return_counts=True
)

area_mais_popular = interesses_unicos[numpy.argmax(contagem)]

print('Regiões dos participantes: ', regioes)
print('Afiliações dos participantes:')

for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {', '.join(nomes)}')

print('Área de interesse mais popular:', area_mais_popular)
