from db import conexao_banco # Importa a função de conexão com o banco de dados

conexao = conexao_banco() # Estabelece a conexão com o banco de dados
if conexao.is_connected():   
    cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
    
    nome_consulta = input("Digite o nome para consulta: ") # Solicita o nome do cliente para consulta

    sql = "SELECT id,nome,telefone,gmail,data_nascimento,senha FROM cliente WHERE nome = %s" # Comando SQL para selecionar o cliente pelo nome
    
    cursor.execute(sql, (nome_consulta,)) # Executa o comando SQL com o nome fornecido
    
    cliente = cursor.fetchone() # Busca o primeiro resultado da consulta
    
    if cliente:
        print("ID:", cliente[0])
        print("Nome:", cliente[1])
        print("Telefone:", cliente[2])
        print("Gmail:", cliente[3])
        print("Data de Nascimento:", cliente[4])
        print("Senha:", cliente[5])
    else:
        print("Cliente não encontrado.")
