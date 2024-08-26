
texto = 'Luciano Lopes Ferreira      '

texto2 = texto.capitalize()
# capitalize muda o primeiro caracter da string para maiusculo
print(texto.capitalize())

# lower padroniza a string em minusculo

nome = 'LuCiAnO LoPes FerReiRa'
nome2 = 'luciano lopes ferreira'


if nome.lower() == nome2.lower():
    print('são iguais')
else:
    print('Não são iguais')

# UPPER padronza uma string em maiusculas

print(nome.upper())

# replace muda um padrão de caracteres de uma string

silvano_sales = 'coração coração cabeção '

# silvano_sales2 = silvano_sales.replace('ç','c')
# silvano_sales2 = silvano_sales2.replace('ã', 'a')

print(silvano_sales.replace('çã', 'ca'))

# strip remove caracteres em branco no final e no inicio de uma string

jack_stripador = '       removendo espaços de uma string       '

print(jack_stripador)
print(jack_stripador.strip())

# split divite uma string em elementos de uma lista

string_espalhada = 'Luciano lopes ferreira'

print(string_espalhada)
print(string_espalhada.split())

# join transforma os elementos de uma lista em uma string
# concatena strings

nome_lista = ['luciano', 'lopes', 'ferreira'] 

# print(' '.join(nome_lista), '\n')

dominio = '@aluno.senai.br'

# slice manipula string por indice

cidade = 'Recando das emas, cidade do povo'

print(cidade[::-1])

palindromo = 'Arara'

if palindromo.lower() == palindromo[::-1].lower():
    print('é palindromo')
else:
    print('não é palindromo')

