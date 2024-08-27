
cavaleiros = ['Seya','Aldebaran', 'Aldebaran', 'Shun', 'Shiryu', 'Yoga' ]

print(cavaleiros)

# adiciona um novo elemento ao final da lista
cavaleiros.append('Ikki')
print(cavaleiros)

# extendendo a lista com outra lista
cavaleiros.extend(['Shina', 'Maryn'])
print(cavaleiros)

# inserir na lista em uma posição especifica
cavaleiros.insert(0,'Athena')
print(cavaleiros)

# remove, exclui um elemento pelo valor.
cavaleiros.remove('Shun')
print(cavaleiros)

# pop - exclui o ultimo elemtno da lista ou o indice informado
elemento = cavaleiros.pop() 
cavaleiros.pop(0)
print(cavaleiros)
print(elemento)

# indice - retorna o indice da primeira ocorrencia de um valor procurado
print(cavaleiros.index('Yoga'))

cavaleiros.pop(cavaleiros.index('Yoga'))
print(cavaleiros)

# Alterando valor de um elemento da lista
cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
print(cavaleiros)

# contabilizando quantidade de elementos repetidos
print(cavaleiros.count('Aldebaran'))

# sort ordena a lista de forma crescente
frutas = ['morango', 'maçã', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota']

numeros = [ 9 , 5 ,81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

# inverte a ordem da lista
frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)

# exclui um lista por completo ou um elemento especifico.
del frutas[0]
print(frutas)

del frutas
print(frutas)

# Limpa a lista
frutas.clear()
print(frutas)
