#Aula13 - Desafio 052

num = int(input('Digite um número: '))

if num == 1:
    print('Esse número não é um número primo')

elif num == 2:
    print('Esse número é um número primo')

elif (num % 2 != 0) and (num % 1 == 0) and (num % num == 0):
    print('Esse número é um número primo!')

else:
    print('Esse número não é um número primo')

print('Fim do programa')
