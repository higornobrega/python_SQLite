import sqlite3
con = sqlite3.connect('banco.db')
cursor = con.cursor()

listaDados = [('Bruno', 25, '00000000000', 'bruno@gmail.com', '84-99999-9999', 'Caico', 'RN', '2019-05-24'),
                ('Paulo', 20, '11111111111', 'paulo@gmail.com', '84-88888-9999', 'Caico', 'RN', '2019-04-20'),
                ('Joao', 22, '22222222222', 'joao@gmail.com', '84-99999-7777', 'Caico', 'RN', '2019-05-15')]

# Cria uma tabela
cursor.execute("""
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado DATE NOT NULL
);
""")

# Insere valores a uma tabela
cursor.execute("""
INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado)
VALUES('Bruno', 25, '00000000000', 'bruno@gmail.com', '84-99999-9999', 'Caico', 'RN', '2019-05-24')
""")

# Insere valores a uma tabela usando uma lista
cursor.executemany("""
INSERT INTO clientes(nome, idade, cpf, email, fone, cidade, uf, criado)
VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", listaDados)

# Faz o commit no banco
con.commit()
print('Dados inseridos com sucesso.')

# Fecha conexao com o banco
#print("Tabela criada com sucesso!")
con.close()
