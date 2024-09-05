# 53. Escreva um programa que peça ao usuário um número e exiba 
# a contagem regressiva desse número até 1.
from os import system
import time

numero = int(input('Informe o numero: '))

while numero >= 1:
    system('clear')
    print(numero)
    numero -= 1
    time.sleep(1)
