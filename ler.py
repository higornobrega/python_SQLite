# Script para ler os dados
import sqlite3

con = sqlite3.connect('banco.db')
cursor = con.cursor()

cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
    print(linha)

con.close()
