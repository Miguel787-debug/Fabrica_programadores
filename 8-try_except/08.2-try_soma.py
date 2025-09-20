# Programa que solicita dois números ao usuário, tenta somá-los e trata erros de entrada

# Entrada de dados do usuário
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

# Tentativa de converter as entradas para inteiros e somá-los
try:
    num1 = int(num1)
    num2 = int(num2)

    # Exibir o resultado da soma
    print(f"A soma dos números é: {num1 + num2}")

# Tratamento de qualquer exceção que possa ocorrer
except:
    print("Digite um número correto!")
