# Programa para registrar múltiplos nomes e e-mails em um arquivo texto

letra = "s" # Inicializa a variável para entrar no loop
while letra.lower() == "s":
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")

    # Abre (ou cria) o arquivo 'pessoa.txt' no modo de anexação ('a') e escreve os dados
    arquivo = open("09.2-cadastro.txt", "a", encoding="utf-8")
    arquivo.write(f"{nome} | {email}\n")
    arquivo.close() # Fecha o arquivo após a escrita
    
    # Pergunta ao usuário se deseja continuar cadastrando
    letra = input("Deseja realizar um novo cadastro - [S/N]: ")

print("Cadastro encerrado.") # Indica que o processo de cadastro foi finalizado
