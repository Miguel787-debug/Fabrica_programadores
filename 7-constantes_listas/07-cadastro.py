NOME_PROGRAMA = "Agenda de Contatos" # Nome do programa

agenda = [] # lista para armazenar os contatos

def cadastrar_contato(nome):
    agenda.append(nome) # adiciona o contato à agenda
    print(f"Contato '{nome}' cadastrado com sucesso")


def listar_contatos():
    print("Lista de Contatos: ")
    print(agenda) # exibe a lista de contatos
    

def remover_contato():
    contato_removido = input("Digite o nome do contato a ser removido: ")
    if contato_removido in agenda:
        agenda.remove(contato_removido)
        print(f"Contato '{contato_removido}' removido com sucesso")
    else:
        print(f"Contato '{contato_removido}' não encontrado na agenda")
        
def main():
    while True:
        print(NOME_PROGRAMA)
        print("-" * 20)
        print("Menu: ")
        print("1.Cadastrar Contato")
        print("2.Listar Contatos")
        print("3.Remover Contato")
        print("4.Sair")
        print("-" * 20)
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Digite um nome para incluir na agenda: ")
            cadastrar_contato(nome)
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            remover_contato()
        elif opcao == 4:
            break
        else:
            print("Opção invalida, tente novamente")
            
            
if __name__ == "__main__":
    main()

            