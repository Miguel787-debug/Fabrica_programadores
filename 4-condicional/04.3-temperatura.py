# Programa que verifica a temperatura e imprime uma mensagem apropriada

# Entrada de dados
temperatura = float(input("Digite a temperatura em Celsius: "))

# Verificação da temperatura
if temperatura >= 30:
    print(f"{temperatura}°C - Está quente!")
elif temperatura >= 20:
    print(f"{temperatura}°C - Está agradável.")
elif temperatura >= 10:
    print(f"{temperatura}°C - Está frio!")
else:
    print(f"{temperatura}°C - Está muito frio!")
