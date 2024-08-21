# Recebendo valores do usuario, convertendo para inteiro e salvando em variaveis
numero1 = int(input('Digite o primeiro numero \n'))
numero2 = int(input('Digite o segundo numero \n'))

# Realizando operação direto na instrução print
print(numero1 + numero2)

# Realizando operação com variaveis dedicadas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# Verificando o tipo de dados das variaveis
print(type(numero1))
print(type(numero2))

# Exemplo de 4 tipos de dados
nome = 'Luciano'
sobrenome ='lopes'
idade = 30
altura = 1.78
vivo = False

# exemplos de concatenação
print('O seu nome completo é '+ nome +' '+ sobrenome)
print('O seu nome completo é', nome , sobrenome)
print(f'O seu nome completo é {nome} {sobrenome}')

print('A soma é: ', soma )
print('A subtracao é: '+ str(subtracao))
print('A multiplicacao é: {} e a divisão foi {}'.format(multiplicacao, divisao))
print(f'A multiplicacao é: {multiplicacao} e a divisão foi {divisao}')

# Resultados simples sem concatenação
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)

# Conversores de dados
int()
float()
str()
bool()

# Convertendo variavel boleana em inteiro
print(int(vivo))

# Verificando tipos
print(type(nome))
print(type((idade)))
print(type(altura))
print(type(int(vivo)))
