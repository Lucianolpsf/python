numeros_pares = list()
# numeros_pares = []

for i in range(10):
    numero = int(input('Informe o numero: '))
    
    if numero % 2 == 0:
        numeros_pares.append(numero)

print('Os numeros pares são: ', sorted(numeros_pares)) 