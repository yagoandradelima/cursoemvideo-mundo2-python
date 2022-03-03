#Aula14 - Desafio 063

#Não está correto, ele só consegue pegar uma parte do código
#Minha estratégia não funciona pra fibonacci, vou tentar fazer sozinho depois

#Esse código não funciona e eu vou corrigir ele

x = 0
y = 1

print('-' * 25)
print('Sequência de fibonacci')
print('-' * 25)
termos = int(input('Quantos termos você quer mostrar? '))

while termos != 0:
    z = x + y
    if termos == 1:
        print(x)
        termos = int(input('Quantos termos a mais você quer mostrar? '))
    if termos == 2:
        print(x)
        print(y)
        termos = int(input('Quantos termos a mais você quer mostrar? '))
    if termos > 2:
        print(z)
        x = y
        y = z           
    termos = int(input('Quantos termos a mais você quer mostrar? '))
print('fim do programa')
            

