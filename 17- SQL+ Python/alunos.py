import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"   
)

cursor = conexao.cursor()
def adicionar_aluno(nome, idade, email):
    sql = "INSERT INTO alunos (nome, idade, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, idade, email))
    conexao.commit()
    print(f"Aluno {nome} adicionado com sucesso.")

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    for linha in cursor.fetchall():
        print(linha)

def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    print(f"Aluno com ID {id} deletado com sucesso!")

def atualizar_aluno(id, novo_nome, nova_idade, novo_email):
    sql = "UPDATE alunos SET nome = %s, idade = %s, email = %s WHERE id = %s"
    cursor.execute(sql, (novo_nome, nova_idade, novo_email, id))
    conexao.commit()
    print(f"Aluno atualizado com sucesso!")

if __name__ == "__main__":

    #adicionar_aluno("Daniel de Souza", 17,"daniel@icloud.com ")
    #listar_alunos()
    #deletar_aluno(3)
    #atualizar_aluno(2, "Luiz Cypriano", 41, "luiscypriano@icloud.com" )
    cursor.close()    
conexao.close()