import sys

def collatz(number):
    if number % 2 == 0:
        retorno = number//2
    else:
        retorno = 3*number+1
    print(str(retorno))
    return retorno
try:
    number = int(input())
except ValueError:
    print('Um numero inteiro deve ser fornecido')
    sys.exit()


while number != 1:
    number = collatz(number)

