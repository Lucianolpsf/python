dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']

for indice, dia in enumerate(dias):
    print(f'{indice + 1} - {dia}')

numero = int(input('Informe seu numero de 1 a 7: '))

print(f'Seu dia é: {dias[numero - 1]}')
