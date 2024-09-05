# 6. Desenvolva um programa que pergunte ao usuário uma operação 
# matemática (+, -, *, /) e dois números, e realize a operação escolhida.

numero1 = int(input("Informe o primeiro numero: "))
operacao = input('Informe a operação +  -  *  / ')
numero2 = int(input("Informe o segundo numero: "))

# match operacao:
#     case '+':
#         print(f'numero {numero1} {operacao} {numero2}, é: {numero1 + numero2}')
#     case '-':
#         print(f'numero {numero1} {operacao} {numero2}, é: {numero1 - numero2}')
#     case '*':
#         print(f'numero {numero1} {operacao} {numero2}, é: {numero1 * numero2}')
#     case '/':
#         print(f'numero {numero1} {operacao} {numero2}, é: {numero1 / numero2}')
#     case _:
#         print('Operação invalida')

# Definição das operações em um dicionário
operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# Verifica se a operação é válida e realiza o cálculo
if operacao in operacoes:
    resultado = operacoes[operacao](numero1, numero2)
    print(f'numero {numero1} {operacao} {numero2}, é: {resultado}')
else:
    print('Operação inválida')


