# Programa que recebe informações sobre um carro e as imprime formatadas

# Criação das variáveis que recebem os valores do usuário
nome_carro = input("Digite o nome do carro: ")
valor_carro = float(input("Digite o valor do carro: "))
consumo_por_litro = float(input("Digite o consumo por litro: "))

# Impressão dos valores formatados
print("------------------------------")
print("| Carro:", nome_carro)
print("| Valor:", valor_carro)
print("| Consumo por litro:", consumo_por_litro)
print("------------------------------")
