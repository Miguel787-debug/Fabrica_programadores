# API de cotação de moedas, usando requests
import requests

awesome_api = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL" # API gratuita de cotações
requisicao = requests.get(awesome_api) # faz a requisição
print(requisicao) 
# obtém as cotações
dolar_real = float(requisicao.json()['USDBRL']['bid'])
euro_real = float(requisicao.json()['EURBRL']['bid'])
bitcoin_real = float(requisicao.json()['BTCBRL']['bid'])

# Solicita o valor em real
valor_real = float(input("Digite o valor em R$ "))

# Mostra o valor convertido, formatado com 2 casas decimais
print(f"R$ {valor_real:.2f} em dólar $ {valor_real / dolar_real:.2f}")
print(f"R$ {valor_real:.2f} em euro € {valor_real / euro_real:.2f}")
print(f"R$ {valor_real:.2f} em bitcoin B {valor_real / bitcoin_real:.2f}")