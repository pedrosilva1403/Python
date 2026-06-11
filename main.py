import mysql.connector

# 1. Estabelecer a conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="318546_Pedr",
    database="cambio"
)
if conexao.is_connected():
    print("Conexão bem-sucedida!")
# 2. Criar o cursor para executar comandos
cursor = conexao.cursor()

# 3. Executar uma consulta SQL (Exemplo: Leitura de dados)
cursor.execute("select * from br_bcb_taxa_cambio_taxa_cambio where moeda='USD'")

# 4. Recuperar os resultados da consulta
resultados = cursor.fetchall()
for linha in resultados:
    print(f"ID: {linha[0]} | Nome: {linha[1]}")

# 5. Fechar os objetos de comunicação
cursor.close()
conexao.close()
