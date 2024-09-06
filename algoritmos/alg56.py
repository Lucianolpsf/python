# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer 
# que uma mensagem seja exibida, e utilize um laço while para exibir 
# a mensagem a quantidade de vezes desejada.
mensagem = input('Qual é a mensagem desejada:')
quantidade = int(input('Informe a quantidade de repetições desejada: '))

while quantidade >= 0:
    print(mensagem)
    quantidade -= 1