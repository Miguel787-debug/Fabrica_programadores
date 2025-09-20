letra = 's'
while letra.lower() == 's': # Use .lower() para aceitar 's' ou 'S'

    try:
        cotacao = float(input('Digite a cotação do dólar: '))

        # Validação para cotação zero, evitando ZeroDivisionError
        if cotacao <= 0:
            print("A cotação do dólar deve ser um valor positivo e maior que zero. Por favor, tente novamente.")
            continue # Volta para o início do loop para pedir os dados novamente

        print("---------------------------------------------------------")
        print("---------------Escolha uma Opção-------------------------")
        print("---------------------------------------------------------")

        opcao = int(input('1 - Converter dólar para real | 2 - Converter real para dólar: '))

        if opcao == 1:
            valor = float(input('Digite o valor em dólar a ser convertido para real: '))
            if valor < 0:
                print("O valor a ser convertido deve ser positivo. Por favor, tente novamente.")
                continue
            resultado = valor * cotacao
            print(f"O valor em reais é: R$ {resultado:.2f}") # Formatado para 2 casas decimais
        elif opcao == 2:
            valor1 = float(input('Digite o valor em reais a ser convertido para dólar: '))
            if valor1 < 0:
                print("O valor a ser convertido deve ser positivo. Por favor, tente novamente.")
                continue
            resultado1 = valor1 / cotacao
            print(f"O valor em dólar é: US$ {resultado1:.2f}") # Formatado para 2 casas decimais
        else:
            print('Opção inválida. Por favor, digite 1 ou 2.')

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números para cotação e valores, e 1 ou 2 para a opção.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

    letra = input('Deseja continuar [S/N]: ').lower() # Converte a resposta para minúscula
    if letra not in ['s', 'n']:
        print("Opção inválida para continuar. O programa será encerrado.")
        break # Sai do loop se a opção de continuar for inválida

print("Programa de conversão encerrado.")