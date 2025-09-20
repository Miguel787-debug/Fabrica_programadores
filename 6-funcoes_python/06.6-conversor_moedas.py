# Função converter dólar para real

def dolar_real(valor_dolar):
    taxa_cambio = 5.10  # taxa de câmbio
    valor_real = valor_dolar * taxa_cambio
    return (valor_real)

# Função converter real para dólar
def real_dolar(valor_real):
    taxa_cambio = 5.10  # taxa de câmbio
    valor_dolar = valor_real / taxa_cambio
    return (valor_dolar)

# Menu interativo
def menu():
    while True:
        print("\n=== Conversor de Moedas ===")
        print("1 - Dólar para Real")
        print("2 - Real para Dólar")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ") # Lê a opção do usuário

        if opcao == "1":
            valor = float(input("Digite o valor em Dólar $  "))
            resultado = dolar_real(valor)
            print(f"$ {valor} = R$ {resultado}")
           
        elif opcao == "2":
            valor = float(input("Digite o valor em Real R$ "))
            resultado = real_dolar(valor)
            print(f"R$ {valor} = $ {resultado}")

        elif opcao == "0":
            print("Obrigado por usar o Conversor de Moedas!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
