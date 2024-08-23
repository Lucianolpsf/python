numero1 = int(input('Informe o primeiro numero: '))
numero2 = int(input('Informe o segundo numero: '))
operacao = input('Informe suaoperação "*" , "/" , "+", "-" :')


match operacao:
    case '*' :
        print('a multiplicação: ', numero1 * numero2)    
    case  '/': 
        print('a divisão: ', numero1 / numero2)    
    case  '+':
        print('a soma: ', numero1 + numero2)    
    case  '-':
        print('a subtração: ', numero1 - numero2)    
    case _:
        print('Operação invalida')
