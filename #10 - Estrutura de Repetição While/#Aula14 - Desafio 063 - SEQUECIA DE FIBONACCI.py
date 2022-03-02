#Aula14 - Desafio 063

x = 0
y = 1

print('-' * 25)
print('Sequência de fibonacci')
print('-' * 25)
termos = int(input('Quantos termos você quer mostrar? '))

while termos != 0:
    for i in range(0, termos):
        if termos == 1:
            print(x)
            termos = int(input('Quantos termos você quer mostrar? '))
        elif termos == 2:
            print(y)
            termos = int(input('Quantos termos você quer mostrar? '))
        elif termos > 2:
            x += y
            y += x
            
            

