print("Converte Celsius para Fahrenheit")

try:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}°F')

except ValueError:
    # Este bloco é executado se o usuário digitar algo que não é um número
    print("Entrada inválida. Por favor, digite um número para a temperatura.")
except Exception as e:
    # Um tratamento mais genérico para outros erros inesperados (improvável aqui, mas boa prática)
    print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")