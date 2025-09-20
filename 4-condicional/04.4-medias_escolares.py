# Sistema de Avaliação de Desempenho Escolar

# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição da média
print(f"\nAluno: {nome}")
print(f"Média: {media}")

# Verificação da situação
if media >= 7:
    print("Resultado: Aprovado ✅")
elif media > 4:
    print("Resultado: Em Recuperação ⚠️")
else:
    print("Resultado: Reprovado ❌")
