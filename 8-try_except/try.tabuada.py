try:
    base = int(input("Digite a base para ver sua tabuada: "))
    inicio = int(input("Digite o início da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))

    # Validação para garantir que o 'fim' não seja menor que o 'inicio'
    if inicio > fim:
        print("O valor de 'início' não pode ser maior que o valor de 'fim'. Por favor, tente novamente.")
    else:
        print(f"--- Tabuada do {base} ")

        i = inicio # Inicializa o contador 'i' com o valor de início

        while i <= fim: # O loop continua enquanto 'i' for menor ou igual ao 'fim'
            print(f"{base} x {i} = {base * i}")
            i += 1 # Incrementa 'i' em 1 a cada iteração

except ValueError:
    print("Entrada inválida! Por favor, digite apenas números inteiros para a base, início e fim.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")