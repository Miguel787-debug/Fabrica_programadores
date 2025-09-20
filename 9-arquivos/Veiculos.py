import csv

dados = 'veiculos.csv'
with open(dados,'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)

    print("dados dos veiculos :\n")
    print('-'*30)
    for linha in leitor:
         print(linha)
