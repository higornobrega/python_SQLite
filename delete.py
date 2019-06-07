import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

id_cliente = 5

# excluindo um registro da tabela
cursor.execute("""
DELETE FROM clientes
WHERE id = ?
""", (id_cliente,))

conn.commit()

print('Registro excluido com sucesso.')

conn.close()