numeros_extenso = ['um', 'dois', 'três']

numero = int(input('Informe um numero de 1 a 3'))

if numero < 1 or numero > 3:
    print('numero invalido')
else: 
    print(f'Seu numero por extenso é: {numeros_extenso[numero-1]} ')