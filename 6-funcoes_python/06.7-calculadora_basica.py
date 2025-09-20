# Função para adição

def adicao(a, b):
    return a + b

# Função para subtração
def subtracao(a, b):
    return a - b

# Função para multiplicação
def multiplicacao(a, b):
    return a * b

# Função para divisão (com verificação de divisão por zero)
def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

# Menu interativo principal
def menu():
    while True:
        print("\n=== Calculadora Básica - NovoTech ===")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora. Até a próxima!")
            break

        if opcao in ["1", "2", "3", "4"]:
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = adicao(num1, num2)
                operacao = "+"
            elif opcao == "2":
                resultado = subtracao(num1, num2)
                operacao = "-"
            elif opcao == "3":
                resultado = multiplicacao(num1, num2)
                operacao = "*"
            elif opcao == "4":
                resultado = divisao(num1, num2)
                operacao = "/"

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
