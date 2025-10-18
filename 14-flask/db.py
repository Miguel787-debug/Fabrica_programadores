import mysql.connector # Conexão com o banco de dados

def conexao_banco(): # Função para estabelecer a conexão com o banco de dados
    conexao = mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = '',
        database = 'aula'
    )
    return conexao # Retorna o objeto de conexão
