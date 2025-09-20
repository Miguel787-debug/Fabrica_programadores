# Exemplo de tratamento de exceção ValueError

try:
    numero = int(input("Digite um número inteiro: "))
# 
except ValueError:
    print("Erro: você digitou um valor inválido!")

try:
   
    numero = int(input("Digite um número inteiro: "))
except ValueError as ve:
    print(f"Erro: {ve}")
    