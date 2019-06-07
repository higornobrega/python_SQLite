import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

id_cliente = input('Digite o id do Cliente: ')
novo_UF = input('Digite nova UF: ')
novo_criado_em = input('Criado em (yyyy-mm-dd): ')

# alterando os dados da tabela
cursor.execute("""
UPDATE clientes
SET fone = ?, criado = ?
WHERE id = ?
""", (novo_UF, novo_criado_em, id_cliente))

conn.commit()

print('Dados atualizados com sucesso.')

conn.close()