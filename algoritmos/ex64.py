lista =[]

for i in range(10):
    numero = int(input('fornceça numero'))
    if numero % 3 == 0:
        lista.append(numero)

for numero in lista:
    print(numero) 