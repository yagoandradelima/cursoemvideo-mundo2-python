#Aula15 - Desafio 068
from random import randint
c = 0
print('-='*10)
print('\033[7mJOGO DO PAR OU ÍMPAR\033[m')
print('-='*10)
while True:
    nUser = int(input('Diga um valor: '))
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Par ou Impar [P/I]?')).upper().strip()[0]
    nPC = randint(0, 10)
    soma = nUser + nPC
    if soma % 2 == 0 and choice == 'P':
        print()
        print(f'Acertou! Eu escolhi o número {nPC} e a soma deu {soma}')
        print('Vamos de novo!')
        print('-'*20)    
    elif soma % 2 != 0 and choice == 'I':
        print()
        print(f'Acertou! Eu escolhi o número {nPC} e a soma deu {soma}')
        print('Vamos de novo!')
        print('-'*20)
    else:
        break
    c += 1
print()
print(f'Errou! Eu escolhi o numero {nPC} e a some deu {soma} \nVocê venceu {c} vez(es)!')
print()