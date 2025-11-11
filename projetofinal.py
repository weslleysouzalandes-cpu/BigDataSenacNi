## PROJETO UC1 ##

import random
import time
lista_menu=[]
menu_principal={
    1: "Sunomono - salada de pepino japonês",
    2:"Salada massao - tomate, escarola, repolho, batata palha e molho “secreto”\n", 
    3:"Shimeji na chapa - shimeji branco, acucar, sal, shoyu, manteiga e cebolinha\n", 
    4:"Guioza - A massa leva farinha e agua, o recheio eh feito por carne de porco e temperos\n",
    5:"Harumaki - Versão chinesa de rolinho primavera com recheio de: \n repolho, cenoura, broto de bambu, cogumelos shiitake, cebola\n"}

menu_sobremesas= {
    1:"bolo de chocolate - Bolo com massa de chocolate e recheio de brigadeiro\n",
    2:"Mousse de morango com calda de morango e morangos fatiados\n",
    3:"Mitarashi Dango - Bolinhos de arroz cobertos com um molho doce e espesso à base de shoyu (molho de soja), açúcar, mirin e amido de milho\n"}
menu_bebidas={
    1:" Garrafa de coca cola 2 litros\n",
    2:"Garrafa d'agua de 300 ml\n",
    3:"Agua saborizada gazeificada\n"}

gerar_pedidos=random.randint(1,400)

print( "BEM VINDO AO SUSHI - BAR")
## SISTEMA DIZENDO QUAL É O SEU GARCON ###########################
mesas=[0,1,2,3,4,5,6]


garcon_mesa={mesas[1]:"marcos",mesas[2]:"marcos",mesas[3]:"marcos", mesas[4]:"juliano",mesas[5]:"juliano", mesas[6]:"juliano"}

#quem é o seu garcon?
nome=str(input("Por favor, digite o seu nome: "))
digite=int(input("digite o numero da sua mesa de 1 a 6:  "))

print(f"O seu garcon é o {garcon_mesa[digite]}")

########################################################

## fuçoes da escolha dos menus

def menu_p(x):
    escolha_seu_prato= menu_principal[x]
    return escolha_seu_prato


def sobremesa(y):
    escolha_sua_sobremesa = menu_sobremesas[y]
    return escolha_sua_sobremesa

def bebidas(z):
    escolha_sua_bebida= menu_bebidas[z]
    return z


print(" Carregando os cardápios")
time.sleep(10)

print(f"Bem vindo(a) {nome}, seu pedido é o número: {gerar_pedidos}, da mesa {digite}")
      
