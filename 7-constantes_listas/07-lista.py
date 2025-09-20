# Lista inicial
nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial: ", nomes)
print("-" * 30)

# Adicionando elementos
nomes.append("Carlos") # Adiciona ao final
print("Após o append: ", nomes)
print("-" * 30)

nomes.insert(1,"Fernanda") # Adiciona "Fernanda" na posição 1
print("Após insert: ", nomes)
print("-" * 30)

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no índice 2
print("Após modificação: ", nomes)
print("-" * 30)

# Removendo elementos
del nomes[3] # Remove o elemento do índice 3
print("Após del: ", nomes)
print("-" * 30)

nomes.remove("Carlos") # Remove a primeira ocorrência  de "Ana"
print("Após remove: ", nomes)
print("-" * 30)

item_removido = nomes.pop(2) # Remove e retorna o elemento do índice 2
print(f"Após pop (removido '{item_removido}'): ", nomes)
print("-" * 30)

nomes.clear() # Esvazia a lista
print("Após clear: ", nomes)
