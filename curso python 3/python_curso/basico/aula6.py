"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número:')

try:
    converao_inteiro =int(numero)
except:
    print('Isso não é um numero inteiro')

if converao_inteiro % 2 == 0:
    print('O número é par')
elif converao_inteiro % 2 != 0:
    print('O número é impar')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = input('Que horas é? ')
horas_int = int(horas)

if horas_int >= 0 and horas_int <= 11:
    print('Bom dia')

elif horas_int > 11 and horas_int <= 17:
    print('Boa tarde')
else:
    print('Boa noite')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')

elif len(nome) > 5 and len(nome) <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito longo')