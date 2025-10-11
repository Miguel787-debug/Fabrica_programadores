from db import conexao_banco

nome = 'Miguel Adalberto'
telefone ='11 97000-0000'
email = 'migue@gmail.com'
data_nascimento = '2007-11-23'
senha = '123456'

conexao = conexao_banco()
if conexao.is_connected():
    cursor = conexao.cursor()
    sql = '''
    INSERT INTO cliente (nome, telefone, email, data_nascimento, senha) 
    VALUES (%s, %s, %s, %s, %s)
    ''' 
    dados = (nome, telefone, email, data_nascimento, senha)
    cursor.execute(sql, dados)
    conexao.commit()
    
    cursor.close()
    conexao.close()
else:
    print("Erro ao conectar ao banco de dados")
