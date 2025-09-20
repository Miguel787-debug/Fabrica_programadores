# Calculadora simples com tratamento de exceções

letra = 's' # Variável de controle para o loop

# Loop principal que continua a fazer operações
while letra == 's':
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicacao")
    print("4 - divisão")
    print("5 - modulo")
    
    operacao = input('Selecione a operação: ')

   
    try:
        numero1 = float(input('Digite um numero: '))
        numero2 = float(input('Digite o outro numero: '))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        continue 
  

    if operacao == '1':
        soma = numero1 + numero2
        print(f'A soma desses números é: {soma}')

    elif operacao == '2':
        subtracao = numero1 - numero2
        print(f'A subtração desses números é: {subtracao}')

    elif operacao == '3':
        multiplicacao = numero1 * numero2
        print(f'A multiplicação desses números é: {multiplicacao}')

    elif operacao == '4':
        # Início do bloco try-except para divisão por zero
        try:
            divisao = numero1 / numero2
            print(f'A divisao desses números é: {divisao}')
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero!")
        # Fim do bloco try-except para divisão por zero

    elif operacao == '5':
        # Início do bloco try-except para módulo por zero
        try:
            modulo = numero1 % numero2
            print(f'O modulo desses numeros é: {modulo}')
        except ZeroDivisionError:
            print("Erro: Não é possível calcular o módulo por zero!")
        # Fim do bloco try-except para módulo por zero
            
    else:
        print("Opção de operação inválida. Por favor, escolha uma das opções [1-5].")

    letra = input('deseja fazer outra conta?[s/n] ').lower() # Adicionado .lower() para aceitar 'S' ou 's'