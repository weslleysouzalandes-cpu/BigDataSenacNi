# EXERCÍCIO 1
#  Escreva um programa para calcular e imprimir o número de lâmpadas 
# necessárias parailuminar um determinado cômodo de uma residência.
#  Dados de entrada: a potência dalâmpada utilizada (em watts), as 
#  dimensões (largura e comprimento, em metros) do cômodo. 
#  Considere que a potência necessária é de 3 watts por metro 
#  quadrado e a cada 3m² existe um bocal para uma lâmpada.



# potencia=int(input("insira a potência da lampada:"))
# largura=int(input("insira largura desejada em metros:"))
# comprimento=int(input("insira o comprimento desejado em metros:"))

# area= largura*comprimento
# resto=area%potencia
# lampada=int(float(area/potencia)+1)

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
# caixas=area/azulejo
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

combustivel=6.15
km_inicial=int(input('Digite o km inicial: '))
km_final=int(input('Digite o km final: '))
combustivel_inicial=float(input('Digite quantos litros haviam no início: '))
combustivel_final=int(input('Digite quantos litros foram gastos: '))
dinheiro=float(input('Digite qual foi o valor pago a você: '))

odometro= int(km_inicial-km_final)
consumo_gasolina= float(combustivel_inicial-combustivel_final)
valor_gasto= consumo_gasolina*combustivel
lucro= dinheiro-valor_gasto
media= odometro/consumo_gasolina

if valor_gasto < dinheiro:
    print (f"Você teve prejuízo de: {lucro} e sua média é {media}")
elif valor_gasto == 0:
    print(f"Você não teve gasto, pois seu total de lucro foi {lucro} e sua média é {media}")

elif valor_gasto > dinheiro:
    print(f'Você teve um lucro de {lucro} e sua média é {media}')

else:
    print('Houve algum erro, coloque valores possíveis')






    

