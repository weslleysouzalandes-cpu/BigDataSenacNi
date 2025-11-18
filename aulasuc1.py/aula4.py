# EXERCÍCIO 1
#  Escreva um programa para calcular e imprimir o número de lâmpadas 
# necessárias parailuminar um determinado cômodo de uma residência.
#  Dados de entrada: a potência dalâmpada utilizada (em watts), as 
#  dimensões (largura e comprimento, em metros) do cômodo. 
#  Considere que a potência necessária é de 3 watts por metro 
#  quadrado e a cada 3m² existe um bocal para uma lâmpada.



# potencia=int(input("insira a potência da lampada:"))
# largura=float(input("insira largura desejada em metros:"))
# comprimento=float(input("insira o comprimento desejado em metros:"))

# area= largura*comprimento
# resto=area%potencia
# lampada=int(float(area/potencia))

# if resto==0:
#     print(f'a quantidade de lampadas necessárias é: {lampada}')

# else:
#     print(f'você precisará de {lampada+1}')

#EXERCÍCIO 2
#Escreva um programa para ler as dimensões de uma cozinha retangular
#  (comprimento,largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar emtodas as suas paredes 
# (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²


# comprimento= float(input('digite o comprimento da cozinha:'))
# largura= float(input('digite a largura da cozinha:'))
# altura= float(input('digite a altura da cozinha:'))

# paredes= comprimento*altura*2
# parede_lado=largura*altura*2
# chao_e_teto=comprimento*largura*2
# azulejo=1.5

# area=paredes+parede_lado+chao_e_teto
# resto=area%azulejo
# caixas=int(area/azulejo)
# match resto:
#     case 0:
#         print(f'você precisará de: {caixas} caixas')
#     case _:
#         print(f'você precisará de um total de {caixas+1} caixas')

#EXERCÍCIO 3

#Um motorista de táxi deseja calcular o rendimento de seu carro na
#  praça. Sabendo-se que opreço do combustível é de R$ 6,15, 
# escreva um programa para ler: a marcação do odômetro (km) no início 
# do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros.
#  Calcular e escrever: a média do consumo em km/L e o lucro (líquido) 
# do dia.

# combustivel=6.15
# km_inicial=int(input('Digite o km inicial: '))
# km_final=int(input('Digite o km final: '))
# combustivel_inicial=float(input('Digite quantos litros haviam no início: '))
# combustivel_final=int(input('Digite quantos litros foram gastos: '))
# dinheiro=float(input('Digite qual foi o valor pago a você: '))

# odometro= int(km_inicial-km_final)
# consumo_gasolina= float(combustivel_inicial-combustivel_final)
# valor_gasto= consumo_gasolina*combustivel
# lucro= dinheiro-valor_gasto
# media= odometro/consumo_gasolina

# if valor_gasto < dinheiro:
#     print (f"Você teve prejuízo de:\n {lucro} e sua média é {media}")
# elif valor_gasto == 0:
#     print(f"Você não teve gasto, pois seu total de lucro foi {lucro} e sua média é {media}")

# elif valor_gasto > dinheiro:
#     print(f'Você teve um lucro de {lucro} e sua média é {media}')

# else:
#     print('Houve algum erro, coloque valores possíveis')


#EXERCÍCIO 4

#Escreva um programa que leia o código de origem de um produto 
# e imprima na tela a região e sua procedência, conforme a tabela abaixo:


# try:
#     x=int(input('Qual o seu código? Digite por favor: '))

#     if x==1:
#         print('A origem do seu produto é SUL')
#     elif x==2:
#         print('A origem do seu produto é NORTE')
#     elif x==3:
#         print('A origem do seu produto é LESTE')
#     elif x==4:
#         print('A origem do seu produto é OESTE')
#     elif x==5 or x==6:
#         print('A origem do seu produto é NORDESTE')
#     elif x==7 or x==8 or x==9:
#         print('A origem do seu produto é SUDESTE')
#     elif x==10:
#         print('A origem do seu produto é CENTRO-OESTE')
#     elif x==11:
#         print('A origem do seu produto é NOROESTE')
#     else:
#         print('Seu produto é IMPORTADO')
# except ValueError:
#     print('Por favor digite o código do seu produto numerado de 1 a 11!')

# EXERCÍCIO 5

#Escreva um programa que leia as notas das duas avaliações normais e a 
# nota da avaliação optativa dos estudantes de uma turma.
#  Caso o estudante não tenha feito a optativa, deve ser fornecido o 
# valor -1. Calcular a média do semestre considerando que a prova 
# optativa substitui a nota mais baixa entre as duas primeiras avaliações.
#  Escrever a média e mensagens que indiquem se o estudante foi aprovado, 
# reprovado ou se está em recuperação, de acordo com as informações 
# abaixo:
# Aprovado: média >= 6.0
# Reprovado: média < 3.0
# Recuperação: média >= 3.0 e < 6.

# try:
#     print('Bem vindo à calculadora de notas! Primeiro, digite suas duas primeiras notas')

#     notaum=float(input('Digite a sua primeira nota:  '))

#     n_2=float(input('Digite a sua segunda nota:  '))
  

#     media= float((notaum+n_2)/2)
   

#     if media >=6.0:
#         print('PARABÉNS! VOCÊ ESTÁ APROVADO!!')
    
#     elif media<3.0:
#          print(f'Sinto muito, você está reprovado. Sua média é {media}')
#     else:
#         nota3=float(input('Vejo que você ficou de recuperação, por favor, digite a sua terceira nota. Caso não tenha feito, digite -1: '))
#         if nota3 ==-1:
#              print(f'Sinto muito, você está reprovado. Sua nota é: {media}')
#         else:

#             if nota3 > notaum or nota3>n_2 and notaum > n_2:
#                     final1=float((nota3+notaum)/2)
#                     if final1>=6.0:
#                             print(f'Parabéns, você está aprovado" Sua nota final é {final1}')
#                     else:
#                             print('Sinto muito, você está reprovado')
#             elif nota3 > n_2 or nota3 > notaum and n_2 > notaum:
                
#                 final=float((nota3+n_2)/2)
#                 if final>=6.0:
#                     print (f'Parabéns, você está aprovado! Sua nota final é {final}')
#                 else:
#                     print(f'Sinto muito, você está reprovado, sua nota final é {final}')
#             elif n_2==notaum and nota3>notaum or nota3>n_2:
#                  finaldois=float((nota3+notaum)/2)
#                  print(f'sua nota final é {finaldois}')
#             else:
#                 print(f'Sua média final é {media}')
# except ValueError:
#      print('Digite um número para calcular')


# EXERCÍCIO 6
# 
#        Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
# valor zero como positivo
       
try:
    print('Vamos descobrir se o seu número é positivo ou negativo?')

    x=float(input('Digite o seu número: '))

    if x<0:
        print(f'o seu número, {x:.2f} , é NEGATIVO')
    elif x==0:
        print(f'O seu número {x:.2f} é positivo')
    else:
        print(f'O seu número, {x:.2f} , é positivo')
except ValueError:
    print('Digite um número real')




        



    

