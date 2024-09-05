# 51. Crie um programa que peça ao usuário para inserir números até que ele 
# digite o número 0. Ao final, exiba a soma de todos os números inseridos 
# (exceto o 0).

numero = None
total = int()

while numero != 0:
    numero = int(input('Informe o numero: '))
    total += numero

print(f'A soma dos numeros fornecidos é: {total}')