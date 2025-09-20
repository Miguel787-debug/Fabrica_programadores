# Tentamos executar o código que pode gerar erro
try:
    # Solicitamos ao usuário dois números inteiros
    numero1 = int(input("Digite o numerador: "))  # Entrada para o numerador
    numero2 = int(input("Digite o denominador: "))  # Entrada para o denominador

    # Tentamos fazer a divisão
    resultado = numero1 / numero2


    print("Erro: divisão por zero não é permitida.")


except ValueError:
    print("Erro: você precisa digitar apenas números inteiros.")

else:
    print(f"Resultado da divisão: {resultado}")

finally:
    print("Operação finalizada.")
