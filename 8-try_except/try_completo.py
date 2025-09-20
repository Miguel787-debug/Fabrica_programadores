try:
    numero1 = int(input("Digite o numerador: "))
    numero2 = int(input("Digite o denominador: "))
    resultado = numero1 / numero2
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: você precisa digitar apenas números inteiros.")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Operação finalizada.")




# Tentamos executar o código que pode gerar erro
try:
    # Solicitamos ao usuário dois números inteiros
    numero1 = int(input("Digite o numerador: "))  # Entrada para o numerador
    numero2 = int(input("Digite o denominador: "))  # Entrada para o denominador

    # Tentamos fazer a divisão
    resultado = numero1 / numero2

# Caso o erro seja de divisão por zero (denominador = 0)
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")

# Caso o erro seja por algum valor não numérico (digitar letras, por exemplo)
except ValueError:
    print("Erro: você precisa digitar apenas números inteiros.")

# Caso não haja erro, mostramos o resultado
else:
    print(f"Resultado da divisão: {resultado}")

# Este bloco sempre será executado, não importa se houve erro ou não
finally:
    print("Operação finalizada.")
