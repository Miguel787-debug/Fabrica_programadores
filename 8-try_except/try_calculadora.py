letra = 's'
while letra == 's':
    print("[1] adição \n[2] subtração\n[3] multiplicacao\n[4] divisão\n[5] modulo")
    
    n1 = input('Digite a operação que vc quer fazer: ')

    # --- Início do bloco try-except para as entradas numéricas ---
    try:
        numero1 = float(input('Digite um numero: '))
        numero2 = float(input('Digite o outro numero: '))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        # Se ocorrer um erro de valor, pulamos para a próxima iteração do loop
        # Isso evita que o programa continue com valores inválidos
        continue 
    # --- Fim do bloco try-except para as entradas numéricas ---

    if n1 == '1':
        soma = numero1 + numero2
        print(f'A soma desses números é: {soma}')

    elif n1 == '2':
        subtracao = numero1 - numero2
        print(f'A subtração desses números é: {subtracao}')

    elif n1 == '3':
        multiplicacao = numero1 * numero2
        print(f'A multiplicação desses números é: {multiplicacao}')

    elif n1 == '4':
        # --- Início do bloco try-except para divisão por zero ---
        try:
            divisao = numero1 / numero2
            print(f'A divisao desses números é: {divisao}')
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero!")
        # --- Fim do bloco try-except para divisão por zero ---

    elif n1 == '5':
        # --- Início do bloco try-except para módulo por zero ---
        try:
            modulo = numero1 % numero2
            print(f'O modulo desses numeros é: {modulo}')
        except ZeroDivisionError:
            print("Erro: Não é possível calcular o módulo por zero!")
        # --- Fim do bloco try-except para módulo por zero ---
            
    else:
        print("Opção de operação inválida. Por favor, escolha uma das opções [1-5].")

    letra = input('deseja fazer outra conta?[s/n]').lower() # Adicionado .lower() para aceitar 'S' ou 's'