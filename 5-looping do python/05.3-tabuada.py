base = int(input("Qual a base da sua tabuada: "))
inicio = int(input("Por qual número deve iniciar: "))
fim = int(input("Em qual número deve encerrar: "))

for i in range(inicio,fim+1):
    print(f" {i} X {base} = {i*base}")
    print("-----------")