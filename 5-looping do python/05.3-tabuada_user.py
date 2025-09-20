# Exibição da tabuada do 5 usando loop while

# Base da tabuada e intervalo personalizado
base = int(input("Qual a base da sua tabuada: "))
inicio = int(input("Por qual número deve iniciar: "))
fim = int(input("Em qual número deve encerrar: "))

# Exibição da tabuada usando loop for
for i in range(inicio,fim+1):
    print(f" {i} X {base} = {i*base}")
    print("-----------")