# Programa para registrar nome e e-mail em um arquivo texto

# Solicita ao usuário que insira seu nome e e-mail
nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

# Abre (ou cria) o arquivo 'pessoa.txt' no modo de anexação ('a') e escreve os dados
with open("pessoa.txt", "a") as arquivo:
	arquivo.write(nome + "|" + email + "\n") # Utiliza 'with' para garantir que o arquivo seja fechado automaticamente