# Programa para calcular o Índice de Massa Corporal (IMC) e salvar os resultados em um arquivo de texto.

letra = 's'  # Variável de controle para o loop

while letra == 's':  # Loop principal que continua até que o usuário opte por 'n'

    try:
        nome = input("Digite o nome da pessoa: ")
        Altura = float(input('Digite sua altura (ex: 1.75): '))
        Peso = float(input('Digite seu peso (ex: 70.5): '))

        # Validações básicas para evitar divisões por zero ou valores negativos irreais
        if Altura <= 0 or Peso <= 0:
            print("Altura e peso devem ser valores positivos e maiores que zero. Tente novamente.")
            continue  # Volta para o início do loop para pedir os dados novamente

        IMC = (Peso / Altura ** 2)  # Cálculo do IMC
        print(f'O IMC de {nome} é: {IMC:.2f}')  # Exibe o IMC com duas casas decimais

        # Classificação do IMC
        if IMC <= 18.4:
            classificacao = 'Abaixo do peso'
        elif IMC <= 24.9:
            classificacao = 'Peso Adequado'
        elif IMC <= 29.9:
            classificacao = 'Sobrepeso'
        elif IMC <= 34.9:
            classificacao = 'Obesidade Grau 1'
        elif IMC <= 39.9:
            classificacao = 'Obesidade Grau 2'
        else:
            classificacao = 'Obesidade Grau 3'

        print(classificacao)

        # Grava os dados no arquivo
        with open("imc.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome}: IMC = {IMC:.2f} ({classificacao})\n")

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números para altura e peso.")
    except Exception as e:  # Um tratamento mais genérico para outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

    letra = input('Deseja repetir o cálculo [s/n]? ').lower()  # .lower() para aceitar 'S' ou 's'
    while letra not in ['s', 'n']:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        letra = input('Deseja repetir o cálculo [s/n]? ').lower()

print("Cálculo de IMC encerrado. Os resultados foram salvos no arquivo 'imc.txt'.")
