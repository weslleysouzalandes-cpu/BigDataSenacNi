## PROJETO UC1 ##

import random
import time
lista_menu=[]
menu_principal={
    1: "Sunomono - salada de pepino japonês",
    2:"Salada massao - tomate, escarola, repolho, batata palha e molho “secreto”", 
    3:"Shimeji na chapa - shimeji branco, acucar, sal, shoyu, manteiga e cebolinha",
    4:"Guioza - A massa leva farinha e agua, o recheio eh feito por carne de porco e temperos",
    5:"Harumaki - Versão chinesa de rolinho primavera com recheio de: repolho, cenoura, broto de bambu, cogumelos shiitake, cebola"}


menu_sobremesas= {
    1:"bolo de chocolate - Bolo com massa de chocolate e recheio de brigadeiro",
    2:"Mousse de morango com calda de morango e morangos fatiados",
    3:"Mitarashi Dango - Bolinhos de arroz cobertos com um molho doce e espesso à base de shoyu (molho de soja), açúcar, mirin e amido de milho"}
menu_bebidas={
    1:" Garrafa de coca cola 2 litros",
    2:"Garrafa d'agua de 300 ml",
    3:"Agua saborizada gazeificada"}

gerar_pedidos=random.randint(1,400)

print( "BEM VINDO AO SUSHI - BAR")

# ## SISTEMA DIZENDO QUAL É O SEU GARCON ###########################

# mesas=[0,1,2,3,4,5,6]


# garcon_mesa={mesas[1]:"marcos",mesas[2]:"marcos",mesas[3]:"marcos", mesas[4]:"juliano",mesas[5]:"juliano", mesas[6]:"juliano"}

# #quem é o seu garcon?
# nome=str(input("Por favor, digite o seu nome: "))
# digite=int(input("digite o numero da sua mesa de 1 a 6:  "))
# mesa_garcon= garcon_mesa[digite]
# print(f"O srº(a) receberá o atendimento de {mesa_garcon}")

# ########################################################

# comprovante= random.randint(10000000,200000000000)
#                                     ######################### FUNÇÕES ####################



# def menu_p(x):
#     escolha_seu_prato= menu_principal[x]
#     return escolha_seu_prato


# def sobremesa(y):
#     escolha_sua_sobremesa = menu_sobremesas[y]
#     return escolha_sua_sobremesa


# def bebidas(z):
#     escolha_sua_bebida= menu_bebidas[z]
#     return escolha_sua_bebida



#                                     #######  MONTANDO A LISTA DE JANTAR ######
# print(f"Bem vindo(a) {nome} ! \n seu pedido é o número: {gerar_pedidos}, da mesa {digite} e seu atendimento será feito pelo {mesa_garcon}")
# time.sleep(4)



## ESCOLHA DO MENU PRINCPAL
import time


def escolha_menu_p(escolha_menu):
    while escolha_menu!= "0":
        if escolha_menu == "0":
            desejo_final = str(input("Obrigado pela visita! \n caso deseje solicitar algo, por favor, digite 1: "))
            
            if desejo_final == "1":
                print(escolha_menu(escolha_menu))  #  Como fazer para voltar ao inicio do pedido?
            else:
                print(f"Obrigado srº(a) {nome} pela visita, volte sempre!")
                break
        else:
            print("Ótimo!\n Mostrarei as nossas opcoes de bebidas")
            time.sleep(4)
            print(menu_principal)
                
            escolha_prato_1= int(input("Por favor, digite a o numero do prato que deseja:   "))
            print("Carregando...")
            time.sleep(5)
            escolhas=menu_principal[escolha_prato_1]
            lista_menu.append(escolhas)

            print(f"prato escolhido: {escolhas} ")
            final= str(input(f"Deseja mais uma bebida? Caso não deseje, digite 0"))
            if final == "0":
                return "Boa refeição"
                break


escolha_menu= str(input(f" Então, srº(a)  deseja algum prato?\n Caso não deseje, por favor, digite 0 : "))

print(escolha_menu_p(escolha_menu))
print(f"A sua(s) bebida(s) escolhida: {lista_menu}")

      
    



         
## ESCOLHA DA BEBIDA
import time

lista_bebidas=[]
def escolha_bebida(escolha_bebida):
    while escolha_bebida!= "0":
        if escolha_bebida == "0":
            desejo_final = str(input("Obrigado pela visita! \n caso deseje solicitar algo, por favor, digite 1: "))
            
            if desejo_final == "1":
                print(escolha_menu_principal)  #  Como fazer para voltar ao inicio do pedido?
            else:
                print(f"Obrigado srº(a) {nome} pela visita, volte sempre!")
                break
        else:
            print("Ótimo!\n Mostrarei as nossas opcoes de bebidas")
            time.sleep(4)
            print(menu_bebidas)
                
            escolha_bebida_1= int(input("Por favor, digite a o numero da bebida que deseja 1,2 ou 3:   "))
            print("Carregando...")
            time.sleep(5)
            escolhas=menu_bebidas[escolha_bebida_1]
            lista_bebidas.append(escolhas)

            print(f"Bebida escolhida: {escolhas} ")
            final= str(input(f"Deseja mais uma bebida? Caso não deseje, digite 0"))
            if final == "0":
                return "Boa refeição"
                break
         
    

escolha_bebidas= str(input(f" Então, srº(a)  deseja alguma bebida?\n Caso não deseje, por favor, digite 0 : "))

print(escolha_bebida(escolha_bebidas))
print(f"A sua(s) bebida(s) escolhida: {lista_bebidas}")

print("Vamos para o pagamento? ")




##                                 ####### FORMA DE PAGAMENTO ###################
# import time
# import random
# xyz=random.randint(62,93)
# xyz1=random.randint(54,109)
# xyz2=random.randint(98,451)
               
# def pagamento(x,y):
#     if (x == "cartao" and y == "debito") or (x == "cartao" and y == "credito"):
#         resultado = print(f"Por favor, insira ou aproxime o seu cartão de {y} ou aparelho na tela")
#         time.sleep(5)
#         resultado = print(f"Gerando comprovante...")
#         time.sleep(5)
#         resultado = print(f"Pagamento do pedido nº {gerar_pedidos} do(a) cliente {nome}  mesa {digite} efetuado com sucesso!\n Por favor,mostre o comprovante nª {comprovante} ao sair .")
#         resultado = print(f"Obrigado pela visita, seja sempre bem vindo(a)!\n Volte Sempre!")
#     elif x == "dinheiro":
#         resultado = print(f"Por favor, dirija-se ao caixa\n nº do pedido: {gerar_pedidos}\n mesa: {digite}")

#     elif x == "qrcode" or x == "pix":
#         print(f"O seu pagamento pode ser efetuado a partir desse código:\n {xyz}-{xyz1}-{xyz2}")
#         time.sleep(5) 
#         print("carregando...")
#         time.sleep(5)
#         return print(f"O numero do seu comprovante de pagamento é {comprovante}, por favor, apresente na saída")
#     else:
#         print("Por favor, digite uma opcao corretamente")
#         resultado = pagamento_final
#     return resultado

# pagamento_final= str(input(f" Por favor, srº(a) {nome} digite qual será a forma de pagamento: dinheiro, pix ou cartao?)"))

# if pagamento_final == "cartao":
#     forma_de_pagamento=str(input(f" Por favor, srº(a) {nome} digite qual sera a forma de pagamento: debito ou credito?"))
#     print("Aguarde um momento")
#     time.sleep(3)
#     print("Carregando... ")
#     time.sleep(5)
#     pagamento(pagamento_final,forma_de_pagamento)

# else:
#     print(pagamento(pagamento_final,0))
#     print("Obrigado, volte sempre")



                                              ####
