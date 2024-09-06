numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))


if numero1 % 2 == 0 and numero2 % 2== 0:
    print('Ambos os numeros são pares')
else:
    print('Pelo menos um dos numeros é impar')