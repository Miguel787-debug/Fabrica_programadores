from db import conexao_banco # Importa a função de conexão com o banco de dados

conexao = conexao_banco() # Estabelece a conexão com o banco de dados

if conexao.is_connected():  # Verifica se a conexão foi bem-sucedida
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL

    user_id = input("Digite o ID do cliente que deseja atualizar: ") # Solicita o ID do cliente para atualização
    novo_telefone = input("Digite o novo telefone do cliente: ") # Solicita o novo telefone do cliente
    novo_gmail = input("Digite o novo email do cliente: ") # Solicita o novo email do cliente
    nova_data_nascimento = input("Digite a nova data de nascimento do cliente (YYYY-MM-DD): ") # Solicita a nova data de nascimento do clienteno
    nova_senha = input("Digite a nova senha do cliente: ") # Solicita a nova senha do cliente
    novo_nome = input("Digite o novo nome do cliente: ") # Solicita o novo nome do cliente

    sql = '''
        UPDATE cliente 
         SET nome = %s,
            telefone = %s,
            gmail = %s,
            data_nascimento = %s,
            senha = %s
        WHERE id = %s
    
'''
    dados = (novo_nome,novo_telefone, novo_gmail, nova_data_nascimento, nova_senha, user_id)

    cursor.execute(sql, dados) # Executa o comando SQL com os novos dados fornecidos
    conexao.commit() # Confirma as alterações no banco de dados
    print("Cliente atualizado com sucesso.")
    cursor.close() # Fecha o cursor
    conexao.close() # Fecha a conexão com o banco de dados

else:  
     print("Erro ao conectar ao banco de dados")
     exit() 