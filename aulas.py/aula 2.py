# ALUNO: WESLLEY DE SOUZA LANDES PINHEIRO

# EXERCÍCIO 1
# print('BEM VINDO AO EXERCÍCIO 1')
# a=int(input('digite o primeiro valor:'))
# b=int(input('digite o segundo valor:'))
# c=int(input('digite o terceiro valor:'))

# if a<b and b<c:    # é possível fazer com if em sequência e depois ordenar
#     print(a,b,c)
# elif a<b and b>c:
#     print(a,c,b)
# elif a>b and b<c:
#     print(b,c,a)
# elif c<b and b<a:
#     print(c,b,a)
# elif c<a and a<b:
#     print(c,a,b)
# elif b<a and a<c:
#     print(b,a,c)
# else:
#     print('ERROR404!! digite numeros diferentes')

#TOTAL DE 18 LINHAS USADAS PARA ESTE CÓDIGO

#EXERCICIO 2

print('BEM VINDO AO EXERCÍCIO 2!')
print('VAMOS CALCULAR SUA MÉDIA ><')
a=float(input('DIGITE SUA PRIMEIRA NOTA:'))
b=float(input('DIGITE SUA SEGUNDA NOTA:'))
c=float(input('DIGITE SUA TERCEIRA NOTA:'))
d=float(input('DIGITE SUA QUARTA NOTA:'))

media=float((a+b+c+d)/4)

if media>7:
    print('PARABÉNS! VOCÊ ESTÁ APROVADO!')
elif media>=5 and media<=7:
    print('Você está de Recuperação')
else:
    print('Reprovado, tente novamente!')

#TOTAL DE 14 LINHAS USADAS PARA ESSE CÓDIGO