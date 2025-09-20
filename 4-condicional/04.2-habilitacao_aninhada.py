#

# Entrada de dados
nome = input("Qual é o seu nome? ")
idade = int(input("Qual sua idade? "))
possui_carteira = int(input("Possui carteira de motorista? \n(1-Sim / 2-Não) "))

# Verificação da idade e carteira de motorista
if idade >= 18:
    if possui_carteira == 1:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    print("Menor de idade")
