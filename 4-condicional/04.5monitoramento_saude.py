# Monitoramento de Saúde - Cálculo do IMC

# Entrada de dados
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc}")

if imc < 18.5:
    print("Condição: Abaixo do peso ⚠️")
elif imc < 24.9:
    print("Condição: Peso normal ✅")
elif imc < 29.9:
    print("Condição: Sobrepeso ⚠️")
elif imc < 34.9:
    print("Condição: Obesidade Grau I ❗")
elif imc < 39.9:
    print("Condição: Obesidade Grau II ❗❗")
else:
    print("Condição: Obesidade Grau III (mórbida) 🚨")

if imc >= 30.0:
    print("Mensagem: Cuidado com a Saúde ⚠️")
else:
    print("Mensagem: Tudo ok 👍")
