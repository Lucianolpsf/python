# numeros = [1 , 5, 8, 10, 3, 78, 100, 51]

# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(sum(numeros))

# media = sum(numeros) / len(numeros)

# print(media)

# # recebe uma lista numerica e calcula a media
# def media (numeros):
#     resultado = sum(numeros) / len(numeros)
#     return resultado

# # uso da função media
# resposta = media(numeros)

# print(resposta)

# função que recebe dois numeros e soma
def soma (a , b) :
    soma = a + b
    return soma


somar = lambda a, b: a + b

print(somar(10, 5))




# # uso da função soma
# print(soma(15, 35))

# # função sem retorno
# def saudacao(nome):
#     print(f'Olá {nome}')

# # uso da função
# saudacao('Luciano')

# # função com parametro opcional
# def ola(nome, mensagem='Olá'):
#     print(mensagem , nome)

# ola('Luciano', 'oi')
# ola('Luciano')

# função com multiplo retorno

def dividir (numero1 , numero2 ):
    resposta = numero1 // numero2
    resto = numero1 % numero2
    return resposta, resto


divisao = dividir(10, 2)

print(divisao)


# numeros = (1 , 5, 8, 10, 3, 78, 100, 51)

# print(type(numeros))


def exibir_informacoes(*args):
    print('Argumentos posicionais: ', args)


# exibir_informacoes(1,4,'Luciano', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos nomeados: ', args)


# exibir_informacoes2(nome='Luciano', idade =30, curso='python')

# key : value
# chave : valor
pessoas =[{
    'nome': 'Luciano',
    'idade': 30,
    'estado_civil': 'casado',
    'escolaridade': 'especialista'
},
{
    'nome': 'Daniel',
    'idade': 19,
    'estado_civil': 'noivo',
    'escolaridade': 'superior'
}]

print(pessoas[1])

import os 

os.system('clear')

print('Luciano', end=' ')
print('Fran', end=' ')
print('Daniel')