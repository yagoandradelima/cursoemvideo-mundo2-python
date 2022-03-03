#Aula14 - Desafio 066

num = int(input('Digite um número: '))
continua = str(input('Deseja continuar[S/N]? ')).strip().upper()         
 
c = 1
soma = num
maior = menor = num

while continua == 'S':
    c += 1
    soma += num
    num = int(input('Digite um número: '))
    continua = str(input('Deseja continuar[S/N]? ')).strip().upper()

    media = soma / c

print(f'media = {media} / ')




    