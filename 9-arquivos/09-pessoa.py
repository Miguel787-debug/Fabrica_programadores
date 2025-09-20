# Programa para registrar nome e e-mail em um arquivo texto

# Solicita ao usuário que insira seu nome e e-mail
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

arquivo = open("pessoa.txt", "a")
arquivo.write(nome + "|" + "\n") 
arquivo.close() 