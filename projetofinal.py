## PROJETO UC1 ##
 #### trabalho do projeto 1 realizado dia 13/11/2025
import random
import time


                                                ###### LISTAS  ###########
lista_menu=["bem vindo à lista"]

lista_bebidas=["bem vindo à lista"]
lista_sobremesas=["bem vindo à lista"]
                                    ############# CARDAPIOS ###############
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

precos_pratos = {"precos":"pratos",menu_principal[1]:10.00 ,menu_principal[2]: 12.00, menu_principal[3]: 20, menu_principal[4]: 25.00,
menu_principal[5]: 25.00}

precos_bebidas = {'precos':'bebidas',menu_bebidas[1]: 8.00, menu_bebidas[2]: 5.00, menu_bebidas[3]: 7.50}
precos_sobremesas = {'precos':'sobremesas',menu_sobremesas[1]: 12.50, menu_sobremesas[2]: 10.90 , menu_sobremesas[3] : 25.00}

lista_de_precos =[]

gerar_pedidos = random.randint(1,400)




print( "BEM VINDO ao restaurante Japonês Tanoshimi")

# ## SISTEMA DIZENDO QUAL É O SEU GARCON ###########################

mesas=[0,1,2,3,4,5,6]


garcon_mesa={mesas[1]:"marcos",mesas[2]:"marcos",mesas[3]:"marcos", mesas[4]:"juliano",mesas[5]:"juliano", mesas[6]:"juliano"}

#quem é o seu garcon?
nome=str(input("Por favor, digite o seu nome: "))
digite=int(input("digite o numero da sua mesa de 1 a 6:  "))
mesa_garcon= garcon_mesa[digite]
print(f"O srº(a) receberá o atendimento de {mesa_garcon}")

# ########################################################

comprovante= random.randint(10000000,200000000000)
#                                     ######################### FUNÇÕES ####################
# # # escolha_menu = str(input(f" srº(a) {nome}  deseja algum prato?\n Caso não deseje, por favor, digite 0 : "))

# # # print(escolha_menu_p(escolha_menu))



#                                     #######  MONTANDO A LISTA DE JANTAR ######
print(f"\nBem vindo(a) {nome} ! \n seu pedido é o número: {gerar_pedidos}, da mesa {digite} e seu atendimento será feito pelo {mesa_garcon}")
time.sleep(4)



# ## ESCOLHA DO MENU PRINCPAL

import time
print("\n"*3)
print(f"\n Bem vindo(a) {nome} ao MENU PRINCIPAL ")
escolha_menu = str(input(f" srº(a) {nome}  deseja algum prato?\n Se sim, pressione ENTER. Caso não deseje, por favor, digite 0 : "))

def escolha_menu_p(escolha_menu):
    
    while escolha_menu != "00":
        if escolha_menu == "0":
            desejo_final = str(input("\n Obrigado pela visita! \n caso deseje solicitar um prato, por favor, digite 1. " \
            "Se não desejar um prato e seguir com o cardápio, digite 00: "))
            
            if desejo_final == "1":
                escolha_menu = str(input(f"\n srº(a)  deseja algum prato?\n Caso não deseje, por favor, digite 0 : "))

                print(escolha_menu_p(escolha_menu))  #  Como fazer para voltar ao inicio do pedido?
            else:
                print(f"\n Tudo bem, então vamos seguir com nosso cardápio!")
                break
        else:
            print("Ótimo!\n Mostrarei as nossas opcoes de pratos principais")
            time.sleep(5)
            print(menu_principal)
            print("\n" *2)
            print(precos_pratos) 
            escolha_prato_1= int(input("\n Por favor, digite a o numero do prato que deseja:   "))
            
            print("Carregando...")
            time.sleep(5)
            escolhas=menu_principal[escolha_prato_1]
            print(f"O preço da sua(s) bebida(s) é {precos_pratos[escolhas]}")
            lista_menu.append(escolhas)
            lista_de_precos.append(precos_pratos[escolhas])
            

            print(f"prato escolhido: {escolhas} ")
            final= str(input(f"\n Deseja mais um prato? Se sim, digite sim. Caso não deseje, digite 0"))
            if final == "0":
                
                print(f"\n Seu(s) prato(s) escolhido foi: {lista_menu}")
                return "\n Boa refeição"
                break

print(escolha_menu_p(escolha_menu))
print("\n"*2)

         
                                                                ## ESCOLHA DA BEBIDA ####
import time

print("\n"*3)
print(f"Bem vindo(a) {nome} ao cardápio de BEBIDAS")
escolha_bebida_inp= str(input(f"\n Então, srº(a) {nome} deseja alguma bebida?Se sim, pressione ENTER. Caso não deseje, por favor, digite 0, caso nao deseje solicitar outro prato digite 00 : "))

lista_bebidas=[]
def escolha_bebida(escolha_bebida_inp):
    while escolha_bebida_inp != "00":
        if escolha_bebida_inp == "0":
            desejo_final = str(input("Obrigado pela visita. Caso deseje solicitar mais um prato, por favor, digite 1." \
            "Caso contrário, por favor, digite 00 : "))
            
            if desejo_final == "1":
                escolha_menu = str(input(f"\n srº(a)  deseja solicitar mais algum prato?\n Caso não deseje, por favor, digite 00 : "))
                print(escolha_menu_p(escolha_menu))
                 #  Como fazer para voltar ao inicio do pedido?
            else:
                
                print(f"\n Tudo bem, vamos prosseguir com nosso cardápio. Mostrarei nossas sobremesas!")
                break
        else:
            print("Ótimo!\n Mostrarei as nossas opções de bebidas")
            time.sleep(4)
            print(menu_bebidas)
            print("\n"*2)
            print(precos_bebidas)    
            escolha_bebida_1= int(input("\n Por favor, digite a o numero da bebida que deseja 1,2 ou 3:   "))
            
            print("\nCarregando...")
            time.sleep(5)
            escolhas=menu_bebidas[escolha_bebida_1]
            print(f"O preço da sua(s) bebida(s) é {precos_bebidas[escolhas]}")
          
            lista_bebidas.append(escolhas)
            lista_de_precos.append(precos_bebidas[escolhas])
            

            print(f"Bebida escolhida: {escolhas} ")
            final= str(input(f"Deseja mais uma bebida? Caso não deseje, digite 0"))
            if final == "0":
                print(f"A sua(s) bebida(s) escolhida: {lista_bebidas}")

                return "Boa refeição"
                break
         
print(escolha_bebida(escolha_bebida_inp))
print("\n")
print("\n"*3)
                                                            ########
                                                        #### ESCOLHA DA SOBREMESA ####

import time
print("\n"*3)
print(f"\n Bem vindo(a) {nome} ao menu de Sobremesas")
escolha_sobremesa_inp = str(input(f" Então, srº(a) {nome} deseja alguma sobremesa?\n Caso não deseje, por favor, digite 0 : "))

lista_sobremesas=[]
def escolha_sobremesa(escolha_sobremesa_inp):
    while escolha_sobremesa_inp != "00":
        if escolha_sobremesa_inp == "0":
            desejo_final = str(input(" Obrigado pela visita! \n caso deseje solicitar bebidas ou queira solicitar um outro prato, por favor, digite 1." \
            "Caso não deseje nem pratos e nem bebidas, por favor, digite 00 : "))
            
            if desejo_final == "1":
                escolha_menu = str(input(f"\n srº(a)  deseja solicitar mais algum prato?\n Caso não deseje, por favor, digite 00 : "))
                print(escolha_menu_p(escolha_menu))

                escolha_bebidas= str(input(f"\n Então, srº(a)  deseja solicitar mais alguma bebida?\n Caso não deseje, por favor, digite 00 : "))
                print(escolha_bebida(escolha_bebidas))
                 #  Como fazer para voltar ao inicio do pedido?
            else:
                print(f"\n Tudo bem, vamos prosseguir com nosso cardápio. Mostrarei nossas sobremesas!")
                break
        else:
            print("Ótimo!\n Mostrarei as nossas opções de sobremesas")
            time.sleep(4)
            print(menu_sobremesas)
            print("\n"*2)
            print(precos_sobremesas)    
            escolha_sobremesa_1= int(input("\n Por favor, digite a o numero da bebida que deseja 1,2 ou 3:   "))
           
            print("\nCarregando...")
            time.sleep(5)
            escolhas=menu_sobremesas[escolha_sobremesa_1]
            
            lista_sobremesas.append(escolhas)
            

            print(f"\n Sobremesa escolhida: {escolhas} ")
            print(f"O preço da sua sobremesa é {precos_sobremesas[escolhas]}")
            lista_de_precos.append(precos_sobremesas[escolhas])
            final= str(input(f"\nDeseja mais uma sobremesa? Caso não deseje, digite 0. Caso deseje retornar, digite: return"))
            if final == "0":
                print(f"\nA sua(s) sobremesa(s) escolhida: {lista_sobremesas}")

                return "Boa refeição"
                break
         
print(escolha_sobremesa(escolha_sobremesa))
print("\n")


                                        ############# CONFIRMAÇÃO DO PEDIDO  #############

print("\n **** PEDIDOS SELECIONADOS **** ")
print(f"\n Seu(s) prato(s)  são: {lista_menu}")
print(f"\nSuas bebidas:  {lista_bebidas}")
print(f"\nSua(s) sobremesa(s): {lista_sobremesas}")
print(f"\nO preço dos seus itens é: {lista_de_precos}")

confirmacao = str(input("O seu pedido está correto? Se sim digite y, caso contrário digite f"))
if confirmacao == "f":
    print("\nTudo bem, deseja retirar algo ou incluir? Caso deseja retirar, digite r, para adicionar digite a")
    retirar=str(input("Digite qual sua escolha, por favor: "))
    
    if retirar == "r":
        print("\nDe qual lista deseja retirar? ")
        pergunta = str(input("Digite qual lista você deseja modificar: (m) para MENU PRINCIPAL, (b) para BEBIDAS e (s) para SOBREMESAS. Se não desejar digite (sair)"))
        print("\n Tudo bem, digite quantos itens deseja retirar:")
        quantidade= int(input("Por favor digite a quantidade: "))
        if pergunta == "m":
            for i in range (1,quantidade):
                print(f"Você está retirando {i} de {quantidade}")
                print("Tudo bem, digite o número que deseja retirar da sua lista, contando cada item a partir de 1")
                print(lista_menu)
                x=int(input("Digite o numero que deseja retirar"))
                print(lista_menu.pop(x))
            lista_final_menu=print(lista_menu)
        elif pergunta == "b":
            for i in range (1,quantidade):
                print(f"Você está retirando {i} de {quantidade}")
                print("Tudo bem, digite o número que deseja retirar da sua lista, contando cada item a partir de 1")
                print(lista_bebidas)
                x=int(input("Digite o numero que deseja retirar"))
                print(lista_menu.pop(x))
            print(lista_bebidas)
        elif pergunta == "s":
            for i in range (1,quantidade):
                print(f"Você está retirando {i} de {quantidade}")
                print("Tudo bem, digite o número que deseja retirar da sua lista, contando cada item a partir de 1")
                print(lista_sobremesas)
                x=int(input("Digite o numero que deseja retirar"))
                print(lista_sobremesas.pop(x))
            print(lista_sobremesas)
        else:
            print(" Tudo bem, vamos dar continuidade ao atendimento")
    elif retirar == "a":

        print("\nDe qual lista deseja adicionar? ")
        pergunta = str(input("Digite qual lista você deseja modificar: (m) para MENU PRINCIPAL, (b) para BEBIDAS e (s) para SOBREMESAS. Se não desejar digite (sair)"))
        print("\n Tudo bem, digite quantos itens deseja retirar:")
        if pergunta == "m":
            escolha_menu = str(input(f" srº(a) {nome}  deseja algum prato?\n Caso não deseje, por favor, digite 0 : "))

            print(escolha_menu_p(escolha_menu))
            
            print(lista_menu)
                        
            print(lista_menu)
        elif pergunta == "b":
            escolha_bebida= str(input(f"\n Então, srº(a) {nome} deseja alguma bebida?\n Caso não deseje, por favor, digite 0 : "))
            print(escolha_bebida(escolha_bebida))

            print(lista_bebidas)
        elif pergunta == "s":
            escolha_sobremesa = str(input(f" Então, srº(a) {nome} deseja alguma sobremesa?\n Caso não deseje, por favor, digite 0 : "))

            print(escolha_sobremesa(escolha_sobremesa))

            print(lista_sobremesas)
        else:
            print("Tudo bem, vamos continuar com o atendimento")







        
    


                                                                ####
elif confirmacao == "y":
    print("Perfeito! Vamos continuar com nosso atendimento")

print("\n" *2 )

print("\nVamos para o pagamento? ")


                                        ###   GARCON RECEBE E ENTREGA O PEDIDO  ###

print(f"\n Olá, garçon {garcon_mesa}. O seu pedido é da mesa {digite} e seu(s) cliente(s) {nome}")

print(f"\n Caso confirme a mesa e o pedido digite (s), caso não confirme digite (n)")

confirmacao_garcon = str(input("Você confirma o recebimento do pedido?"))
def confirmacao(confirmacao_garcon):
    if confirmacao_garcon == "s":
        print("Ótimo. Mostrarei o tempo de preparo dos pedidos aos nossos clientes")
        print("preparando pedido")
        time.sleep(5)
        print("Por favor dê a saída, pressione (s), do pedido para que nosso(s) cliente(s) possa confirmar o recebimento")
        saida = str(input("Dê a saída por favor"))
        if saida == "s":
            resultado = print("Obrigado! Por favor, dirija-se à mesa e sirva nosso(s) cliente(s)")
        else:
            while repeticao != "s":
                resultado = repeticao = str(input("Por favor, dê a saída no pedido"))
                break


    else:
        print("Por favor, passe esta informação para outro garçon")

    return resultado

print(confirmacao(confirmacao_garcon))

                                    ## CONFIRMAÇAO DA ENTREGA DO PEDIDO PELO CLIENTE     #    # 

tempo_pedido = random.randint(1,10)
print(f"Olá srº(a) {nome}, vejo que seu pedido demorará {tempo_pedido} minutos para estar pronto")
time.sleep(3)

print(f"Olá, {nome} novamente! vejo que seu pedido já saiu para entrega em sua mesa {digite} pelo garçon {garcon_mesa[digite]}")
time.sleep(3)

print("Por favor, me diga se o seu pedido foi entregue corretamente pelo garçon")
entrega = str(input("Digite (s) para sim e (n) para não:  "))

if entrega == "s":
    print("Boa refeição! Caso precise, pode chamar um de nossos colaboradores.")

else:
    print("Sinto muito! Deseja fazer um novo pedido?")
    pedido_novo = str(input("Caso deseje fazer um novo pedido, por favor digite sim, caso deseje outras informações solicite a gerência"))
    if pedido_novo == "sim":
        lista_bebidas.clear()
        lista_menu.clear()
        lista_sobremesas.clear()

        escolha_menu = str(input(f" srº(a) {nome}  deseja algum prato?\n Caso não deseje, por favor, digite 0 : "))
        print(escolha_menu_p(escolha_menu))

        print("\n"*3)
        print(f"Bem vindo(a) {nome} ao cardápio de BEBIDAS")
        escolha_bebida= str(input(f"\n Então, srº(a) {nome} deseja alguma bebida?\n Caso não deseje, por favor, digite 0 : "))

        print(escolha_bebida(escolha_bebida))

        print("\n"*3)
        print(f"\n Bem vindo(a) {nome} ao menu de Sobremesas")
        escolha_sobremesa = str(input(f" Então, srº(a) {nome} deseja alguma sobremesa?\n Caso não deseje, por favor, digite 0 : "))
        print(escolha_sobremesa(escolha_sobremesa))
    else:
        print("Tudo bem, caso você deseje falar com a gerência, por favor, solicite ao caixa")


                                    ##   PAGAMENTO ##

time.sleep(3)

print(f"Olá, srº(a) {nome} a partir de agora você entrará na parte do pagamento")
confirma = str(input("Podemos continuar com o pagamento? Se sim, digite y, ou n para não"))






##                                 ####### FORMA DE PAGAMENTO ###################
import time
import random

xyz=random.randint(62,93)
xyz1=random.randint(54,109)
xyz2=random.randint(98,451)

def pagamento(x,y):
    if (x == "cartao" and y == "debito") or (x == "cartao" and y == "credito"):
        resultado = print(f"Por favor, insira ou aproxime o seu cartão de {y} ou aparelho na tela")
        time.sleep(5)
        resultado = print(f"Gerando comprovante...")
        time.sleep(5)
        resultado = print(f"Pagamento do pedido nº {gerar_pedidos} do(a) cliente {nome}  mesa {digite} efetuado com sucesso!\n Por favor,mostre o comprovante nª {comprovante} ao sair .")
        resultado = print(f"Obrigado pela visita, seja sempre bem vindo(a)!\n Volte Sempre!")
    elif x == "dinheiro":
        resultado = print(f"Por favor, dirija-se ao caixa\n nº do pedido: {gerar_pedidos}\n mesa: {digite}")

    elif x == "qrcode" or x == "pix":
        print(f"O seu pagamento pode ser efetuado a partir desse código:\n {xyz}-{xyz1}-{xyz2}")
        time.sleep(5) 
        print("carregando...")
        time.sleep(5)
        return print(f"O numero do seu comprovante de pagamento é {comprovante}, por favor, apresente na saída")
    else:
        print("Por favor, digite uma opcao corretamente")
        resultado = pagamento_final
    return resultado


    
print(f"\n O preço dos seus itens é: {lista_de_precos}")



pagamento_final= str(input(f" Por favor, srº(a) {nome} digite qual será a forma de pagamento: dinheiro, pix ou cartao?)"))

if pagamento_final == "cartao":
    forma_de_pagamento=str(input(f" Por favor, srº(a) {nome} digite qual sera a forma de pagamento: debito ou credito?"))
    print("Aguarde um momento")
    time.sleep(3)
    print("Carregando... ")
    time.sleep(5)
    pagamento(pagamento_final,forma_de_pagamento)

else:
    print(pagamento(pagamento_final,0))
    time.sleep(3)
    print("Obrigado, volte sempre")



                                              ####
