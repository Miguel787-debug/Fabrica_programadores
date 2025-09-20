# Exercício de conversão dos programas de Portugol para Python

# Programa que lê o nome e as três notas de um aluno, calcula a média e imprime o resultado

# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A média do aluno {nome} é {media}")
