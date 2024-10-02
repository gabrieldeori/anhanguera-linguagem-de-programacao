import matplotlib.pyplot as plt
# Classe para representar um livro

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):

        return f'{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}'


biblioteca = []


def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    print(f'"{titulo}" foi adicionado à biblioteca.')


def listar_livros():
    print()
    for livro in biblioteca:
        print(livro)


adicionar_livro('Teste1', 'Eu', 1605)
adicionar_livro('Livro Z', 'Zapat', 1813)
adicionar_livro('Xablauzin e o Xablau', 'Xablau', 1949)
adicionar_livro('Lorem', 'Ipsum', 1967)
adicionar_livro('OMG', 'STOP', 1951)
adicionar_livro('3', '4', 1951)
adicionar_livro('5', '7', 1951)
adicionar_livro('wfwwf', 'ssssfasfw', 1951)

listar_livros()


anos = sorted(list(set(livro.ano_publicacao for livro in biblioteca)))
contagem_por_ano = [
    sum(livro.ano_publicacao == ano for livro in biblioteca) for ano in anos
]


plt.plot(anos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

for i, valor in enumerate(contagem_por_ano):
    plt.text(anos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)
plt.show()
