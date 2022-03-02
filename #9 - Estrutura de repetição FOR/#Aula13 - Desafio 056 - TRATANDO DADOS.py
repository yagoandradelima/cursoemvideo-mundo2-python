#Aula13 - Desafio 056

b = 0
somaIdade = 0

for i in range(0, 4):
    nome = str(input('Digite o nome da pessoa: ')).strip().lower()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    print()
    
    somaIdade += idade

    #Caso o primeiro valor seja o maior, o i == 0 armazena ele já que ele só armazenará algum valor caso o elif mais abaixo seja executado
    if i == 0:
        maior = menor = idade
        n = nome

    elif sexo == 'F' and idade > 20:
        b += 1
        

    elif sexo == 'M' and idade > maior:
        maior = idade
        n = nome

mediaIdade = somaIdade / 4

print()
print(f'A Média de idade do grupo é {mediaIdade:.1f}')
print(f'O homem mais velho possui {maior} anos e tem o nome de {n}!')
print(f'Existem {b} mulheres acima de 20 anos')
print()
