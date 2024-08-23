
# if candidato == 13:
#     print('Votou no Lula')
# elif candidato == 22:
#     print('Votou no Bolsonaro')
# else:
#     print('Candidato invalido')
# match case uma estrutura condicional, alternativa ao if
# abaixo verifica o voto do usuario
# candidato = int(input('Informe o numero do candidato \n'))

# match candidato:
#     case  13:
#         print('votou no Lula')
#     case 22:
#         print('votou no Bolsonaro')
#     case _:
#         print('opção invalida')

#atribuição de valores a uma variavel

# numero = 10
# print(numero)

# #numero = numero + 10
# numero += 10
# print(numero)

# #numero = numero - 10
# numero -= 10
# print(numero)

# #numero = numero * 10
# numero *= 10
# print(numero)

# #numero = numero / 10
# numero /= 10
# print(numero)

# verificando se um numero é par ou impar

# numero = int(input('Informe o numero\n'))

# if numero % 2 == 0:
#     print('numero é par')
# else:
#     print('numero é impar')
    
# laços de repetição for em portugues 'para'

# for i in range(5):
#     print(i)

# nomes = ['Luciano', 'Lucas', 'Arthur', 'Aline', 'Beatriz']

# print(nomes)

# for pessoa in nomes:
#     print(pessoa)

# print(frutas[2])

# for item in frutas:
#     print(item)
# frutas = ['banana', 'maçã', 'morango', 'laranja']

# for indice, fruta in enumerate(frutas):
#     print(f'Suas frutas são {indice}: {fruta} ')
# nomes = []

# for i in range(5):
#     nome = input('Informe o seu nome: \n')
#     nomes.append(nome)

# for nome in nomes:
#     print(nome)

# nome = 'Luciano'

# for i in nome:
#     print(i)

# While em português Enquanto

# numero = None

# while numero != 0:
#     numero = int(input('Informe o numero\n'))

contador = 1
numero = int(input('Informe o numero: '))

while contador < 10:
    print(contador)
    contador +=1

# numero = 10
# while True:
#     numero *= 10 
#     print(numero)
#     if numero > 100000000:
#         break 