from flask import Blueprint, render_template,request # Usado para renderizar as templates de HTML
from db import conexao_banco # Importa a função de conexão com o banco de dados

cliente = Blueprint('cliente', __name__) # Cria um blueprint para organizar as rotas relacionadas ao cliente

@cliente.route('/formulario', methods=['GET', 'POST'])

def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        gmail = request.form['gmail']
        data_nascimento = request.form['data_nascimento']
        senha = request.form['senha']
        
        conexao = conexao_banco() # Estabelece a conexão com o banco de dados
        if conexao.is_connected():   
         cursor = conexao.cursor() # Cria um cursor para executar comandos SQL
            
        sql = '''
            INSERT INTO cliente (nome, telefone, gmail, data_nascimento, senha)
                VALUES (%s, %s, %s, %s, %s)
            ''' # Comando SQL para inserir um novo cliente
            
        dados = (nome, telefone, gmail, data_nascimento, senha)
    
        cursor.execute(sql, dados) # Executa o comando SQL com os dados fornecidos
        conexao.commit() # Confirma as alterações no banco de dados
            
        cursor.close() # Fecha o cursor
        conexao.close() # Fecha a conexão com o banco de dados
    
        return "Cliente cadastrado com sucesso!"
    else:
        print("Erro ao conectar ao banco de dados")