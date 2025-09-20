# Cálculo do IMC com tratamento de exceções

letra = 's' # Variável de controle para o loop

while letra == 's': # Loop principal que continua enquanto até que o usuário opte por 'n'
    
    try:
        Altura = float(input('Digite sua altura (ex: 1.75): '))
        Peso = float(input('Digite seu peso (ex: 70.5): '))

    
        if Altura <= 0 or Peso <= 0:
            print("Altura e peso devem ser valores positivos e maiores que zero. Tente novamente.")
            continue 

        IMC = (Peso / Altura ** 2) 
        print (f'O IMC é: {IMC:.2f}') 

        if IMC <= 18.4:
            print('Abaixo do peso')
        elif IMC <= 24.9:
            print('Peso Adequado')
        elif IMC <= 29.9:
            print('Sobrepeso')
        elif IMC <= 34.9:
            print('Obesidade Grau 1')
        elif IMC <= 39.9:
            print('Obesidade Grau 2')
        elif IMC >= 40:
            print('Obesidade Grau 3')

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números para altura e peso.")
    except Exception as e: # Um tratamento mais genérico para outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.")

    letra = input('Deseja repetir o cálculo [s/n]? ').lower() # .lower() para aceitar 'S' ou 's'
    if letra not in ['s', 'n']:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        # Se você quiser que o loop termine para qualquer coisa diferente de 's',
        # você pode colocar 'letra = 'n'' aqui, ou apenas deixar como está,
        # e o loop só continua se for 's'.

print("Cálculo de IMC encerrado.")