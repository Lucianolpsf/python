nota = float(input('Informe sua nota: '))

if nota > 0.0 and nota < 4.9:
    print('nota baixa')
elif nota >= 5.0 and nota <= 7.9:
    print('nota media')
elif nota >= 8.0 and nota <= 10.0:
    print('nota media')
else:
    print('Nota invalida')
