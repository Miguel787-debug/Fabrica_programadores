import csv
import json

dados = 'veiculos.csv' # Endereço do arquivo CSV
dados_json = 'veiculos.json' # Endereço do arquivo JSON


veiculos = [] # Lista para armazenar os dados dos veículos
with open(dados,'r',encoding = 'utf-8') as arquivo: # Abrir o arquivo CSV para leitura
    leitor = csv.DictReader(arquivo,delimiter=',') # Ler o arquivo CSV como um dicionário

    for linha in leitor: # Iterar sobre cada linha do arquivo CSV
        veiculos.append(linha) # Adicionar cada linha (dicionário) à lista de veículos

with open(dados_json,'w',encoding = 'utf-8') as arquivo_json: # Abrir o arquivo JSON para escrita
        json.dump(veiculos,arquivo_json,indent=4) # Escrever a lista de veículos no arquivo JSON com indentação de 4 espaços
       
print('Arquivo JSON criado com sucesso!') # Mensagem de sucesso