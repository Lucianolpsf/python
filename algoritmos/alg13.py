# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e 
# exiba a estação do ano correspondente.

# primera setembro a dezembro
# verão dezembro março
# outono março a junho
# inverno junho a setembro

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for indice, mes in enumerate(meses):
    print(f'{indice + 1} - {mes}')

mes_escolhido = int(input('Informe o numero do mês escolhido: '))

if mes_escolhido > 2 and mes_escolhido  <7:
    print('Estamos no outono')
elif mes_escolhido > 6 and mes_escolhido  <10:
    print('Estamos no inverno')
elif mes_escolhido > 8 and mes_escolhido  <13:
    print('Estamos na primera')
else:
    print('Estamos no verão primera')

