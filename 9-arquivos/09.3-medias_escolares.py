# Sistema de Avaliação de Desempenho Escolar com Loop e Gravação em Arquivo

# Abrir o arquivo para adicionar dados (cria se não existir)
with open("09.3-medias_escolares.txt", "a", encoding="utf-8") as arquivo:
    while True:
        # Entrada de dados
        nome = input("\nDigite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        # Cálculo da média
        media = (nota1 + nota2 + nota3) / 3

        # Verificação da situação
        if media >= 7:
            resultado = "Aprovado ✅"
        elif media > 4:
            resultado = "Em Recuperação ⚠️"
        else:
            resultado = "Reprovado ❌"

        # Exibição da média e resultado
        print(f"\nAluno: {nome}")
        print(f"Média: {media:.2f}")
        print(f"Resultado: {resultado}")

        # Gravação no arquivo
        arquivo.write(f"Aluno: {nome} | Média: {media:.2f} | Resultado: {resultado}\n")

        # Pergunta se deseja continuar
        continuar = input("\nDeseja calcular a média de outro aluno? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nPrograma encerrado. As médias foram salvas no arquivo.")
            break

