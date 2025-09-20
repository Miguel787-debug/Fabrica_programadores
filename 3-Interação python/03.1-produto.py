# Programa para calcular o preço final de um produto com desconto

# Criação das variáveis que armazenam os dados do produto
nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

# Cálculo do preço final com desconto
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# Exibição do resultado formatado
print(f"Produto: {nome_produto} - Preço final: R$ {preco_final}")
