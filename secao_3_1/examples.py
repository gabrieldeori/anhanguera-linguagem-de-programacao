# Como usar o SQLite

import sqlite3

# 1. Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# 2. Criar um objeto cursor
cursor = conn.cursor()

# 3. Definir o comando SQL para criar a tabela
create_table = """
    CREATE TABLE IF NOT EXISTS Produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER
    );

"""

# 4. Executar o comando SQL para criar a tabela
cursor.execute(create_table)

# 5. Confirmar as alterações (commit)
conn.commit()

# CRUD
# Create

# Dados do novo produto
novo_produto = ('Camiseta', 19.99, 50)

# Comando SQL para inserir o novo produto na tabela
inserir_produto = “INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)”

# Executando o comando SQL para inserção
cursor.execute(inserir_produto, novo_produto)

# Confirmando as alterações
conn.commit()


# Read
selecionar_produtos = “SELECT * FROM Produtos”

# Executando o comando SQL
cursor.execute(selecionar_produtos)

# Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)


# Update

# Novo preço e ID do produto a ser atualizado
novo_preco = 24.99

produto_id = 1  # Suponha que queiramos atualizar o produto com ID 1

# Comando SQL para atualizar o preço do produto
atualizar_preco = “UPDATE Produtos SET preco = ? WHERE id = ?”

# Executando o comando SQL de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))

# Confirmando as alterações
conn.commit()


# Delete

# ID do produto a ser excluído
produto_id = 2  # Suponha que queiramos excluir o produto com ID 2

# Comando SQL para excluir o produto
excluir_produto = “DELETE FROM Produtos WHERE id = ?”

# Executando o comando SQL de exclusão
cursor.execute(excluir_produto, (produto_id,))

# Confirmando as alterações
conn.commit()


# Final. Fechar a conexão com o banco de dados
conn.close()
