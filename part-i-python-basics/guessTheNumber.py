import random

secretNumber = random.randint(1,100)

print('Estou pensando em um número entre 1 e 100.')

# Peça para o jogador adivinhar 6 vezes

for guessesTaken in range(1, 7):
    print('Dê um palpite.')
    guess = int(input())

    if guess < secretNumber:
        print('Palpite baixo')
    elif guess > secretNumber:
        print('Palpite alto')
    else:
        break

if guess == secretNumber:
     print('Boa! você adivinhou o número em ' + str(guessesTaken) + ' palpites!')
else:
     print('Não deu, o número que eu pensei era ' + str(secretNumber))
    
