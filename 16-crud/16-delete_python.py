from db import conexao_banco # Importa a função de conexão com o banco de dados

conexao = conexao_banco() # Estabelece a conexão com o banco de dados
if conexao.is_connected():   
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    
    user_name = input("Digite o nome do cliente que deseja deletar: ") # Solicita o nome do cliente para deleção
    
    sql = "DELETE FROM cliente WHERE nome = %s" # Comando SQL para deletar o cliente pelo nome
    
    dados = (user_name,)
    cursor.execute(sql, dados) # Executa o comando SQL com o nome fornecido
    conexao.commit() # Confirma as alterações no banco de dados
    
    
    if cursor.rowcount > 0:
        print("Usuario excluído com sucesso.")
    else:
        print("Nenhum cliente encontrado com esse nome.")
    
    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados
else:
    print("Erro ao conectar ao banco de dados")