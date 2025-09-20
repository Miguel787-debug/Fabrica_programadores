# Exercício de conversão dos programas de Portugol para Python

# Programa que lê o peso e a altura de uma pessoa, calcula o IMC e imprime o resultado

# Entrada de dados
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

# Cálculo do IMC
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc}")
