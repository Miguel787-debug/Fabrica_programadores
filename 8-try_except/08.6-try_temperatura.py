# Conversão de temperatura com tratamento de exceções

print("Converte Celsius para Fahrenheit")

try:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}°F')

except ValueError:
    
    print("Entrada inválida. Por favor, digite um número para a temperatura.")
except Exception as e:
 
    print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")