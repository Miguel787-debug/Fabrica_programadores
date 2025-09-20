''' 2 - Desenvolva um programa que solicite ao usuário os dados 
de um produto (nome, valor e quantidade) e armazene-os em 
um arquivo de texto chamado "produtos.txt".
'''

letra = 's' # Controla o loop para adicionar múltiplos produtos
while letra == 's':
    nome_produto = input('Digite o nome do produto: ')
    valor_produto = float(input('Digite o valor do produto (em R$): '))
    quantidade_produto = int(input('Digite a quantidade do produto: '))

    # Abre (ou cria) o arquivo 'produtos.txt' no modo de anexação ('a') e escreve os dados
    with open('09.5-produtos.txt', 'a', encoding="utf-8") as arquivo:
        arquivo.write(f"{nome_produto} | R$ {valor_produto:.2f} | Quantidade: {quantidade_produto}\n")
        print(f"Produto {nome_produto} adicionado com sucesso!") # Confirmação de que o produto foi adicionado
    
    # Pergunta se o usuário quer adicionar outro produto
    letra = input('Deseja adicionar outro produto [s/n]? ').lower() 
    if letra not in ['s', 'n']:
        print("Opção inválida. Digite 's' para sim ou 'n' para não.") # Validação simples da entrada
        letra = 'n'