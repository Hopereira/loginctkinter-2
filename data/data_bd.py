import sqlite3
import os
import hashlib
# função para criptografar a senha
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# criando a conexão com o banco de dados
conexao = sqlite3.connect(os.path.abspath("data/data_bd.db"))

# criando o cursor
try:
    cursor = conexao.cursor()
    # criando a tabela de cadastro com email único
    cursor.execute(
       '''CREATE TABLE IF NOT EXISTS usuario
       (id INTEGER PRIMARY KEY AUTOINCREMENT,
       email TEXT NOT NULL UNIQUE,
       senha TEXT NOT NULL,
       c_senha TEXT NOT NULL)'''
    )
    print("Tabela criada com sucesso!")
    conexao.commit()
except sqlite3.Error as e:# tratamento de erro
    print(f"Erro ao criar a tabela: {e}")
    conexao.rollback()# rollback para desfazer a operação
finally:
    conexao.close()# fechando a conexão
