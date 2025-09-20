# Função que sorteia uma tarefa aleatória de uma lista

import random
def sorteio(lista):
    return random.choice(lista)

# apresenta ista de tarefas domésticas após sorteio
print(sorteio(['Lavar o Banheiro', 'Lavar louça', 'Varrer o quintal', 'Retirar o lixo']))
