#Aula12 - Desafio 042 - DESAFIO DOS TRIÂNGULOS V2.0

r1 = float(input('Digite o valor do primeiro lado: '))
r2 = float(input('Digite o valor do segundo lado: '))
r3 = float(input('Digite o valor do terceiro lado: '))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    if r1 != r2 and r2 != r3 and r3 != r1:
        print('As retas podem formar um triângulo retângulo!')
    
    elif r1 == r2 == r3:
        print('As retas podem formar um triângulo equilátero!')
    
    else:
        print('As retas podem formar um triangulo escaleno!')

else:
    print('As retas não podem formar um triângulo!')

print()
print('Fim do Prgrama')