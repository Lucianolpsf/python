maior = None
for i in range(5):
    numero = int(input(f'Informe o numero {i + 1} :'))

    if maior is None or  numero > maior:
        maior = numero

print(f'O maior numero é: {maior}')