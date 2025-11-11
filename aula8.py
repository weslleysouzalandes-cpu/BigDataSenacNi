##Crie um programa que ajude um pescador a controlar sua produtividade.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pel
#  regulamento (100 quilos), ele deve pagar uma multa de R$ 4,00 por quilo excedente.


#CONTROLE DE PRODUTIVIDADE

# lista=[]
# def quilos(x,a=100):
#     "calcular o imposto gerado em caso da quantidade ser maior que 100 "
    
    
#     calculo=(x-a)

#     if calculo >0:
#         resultado= print(f"Sua multa será de: R${round(calculo*4,2)} reais")
#     else:
#         resultado = print("Peso dentro do limite. Nenhuma multa a pagar.")

    
#     return resultado
    
   


# for i in range(3):
#     print(f"Vamos calcular os seus impostos {i+1} de 3 dias")
#     quantidade=int(input("Digite a quantos quilos de peixes que você pescou no final de semana: "))

#     y= quilos(quantidade)
#     lista.append(y)
    
#     print('*'*50)



# print(f'Nos 3 dias você pagou estes impostos{lista}')



### Calculo do IMC ###

# def calc_imc(peso,altura):

#     imc= peso/(altura*altura)
    
#     return imc


# def obter_classificacao(imc):
#     if imc< 18.5:
#         resultado = print(f'Seu imc é {imc}, você está abaixo do peso')
#     elif 18.5<=imc<=24.9:
#         resultado = print(f"Peso normal")
#     elif 25.0<=imc<=29.9:
#         resultado=(f"Você está com Sobrepeso")
#     else:
#         resultado = print("Obesidade")
    
#     return resultado



# total_de_pessoas=int(input('Quantas pessoas precisam calcular seu IMC??  '))

# for i in range(1,total_de_pessoas+1):
#     print(f"\n Você está calculando os dados da pessoa {i} ")
    
#     peso=float(input('Digite o peso (kg) desta pessoa:  '))
#     altura=float(input('Digite a altura(m) desta pessoa em centímetros: '))

#     imc_impresso= calc_imc(peso,altura)
#     classificacao= obter_classificacao(imc_impresso)

#     print(f"O seu imc é {imc_impresso} e sua classificacao é {classificacao} ")


### VAMOS CONVERTER A TEMPERATURA ###

# def celsius_para_f(c):
#     calculo1= ((c*9)/9)+32

#     return calculo1


# def fahrenheit_para_c(f):
#     calculo2=((f-32)*5)/9

#     return calculo2

# conversao= str(input(" Para qual unidade você deseja fazer? celsius ou fahrenheit "))
# temperatura = float(input(" Digite a temperatura:  "))

# resultado_celsius= fahrenheit_para_c(temperatura)
# resultado_f= celsius_para_f(temperatura)

# if conversao== "celsius":
#     print(f"A sua temperatura em celsius é: {resultado_celsius}")
# elif conversao == "fahrenheit":
#     print(f"A sua temperatura em fahrenheit é {resultado_f} ")

# else:
#     print("Digite a temperatura corretamente")


## DESAFIO DA AULA 8, EXERCICIO 3 ##
# def calculo_temp(x,c):
#     if x =="fahrenheit":
#         calculo1= ((c*9)/5)+32
#         resultado=print(f"A sua temperatura é {calculo1}")
#     elif x =="celsius":
#         calculo2=((c-32)*5)/9
#         resultado=print(f"A sua temperatura é {calculo2}")
#     else:
#         resultado=print("Digite uma temperatura corretamente")

#     return resultado

# conversao= str(input(" Para qual unidade você deseja fazer? celsius ou fahrenheit "))
# temperatura = float(input(" Digite a temperatura:  "))

# print(f"A temperatura é: {calculo_temp(conversao,temperatura)}")

#__________________________________________________________________

## EXERCICIO 1 ANO BISSEXTO  ##

def e_bissexto(ano):
    
    ano1= ano%4
    ano100=ano%100
    ano400=ano%400
    if ano1 == 0 and ano100 !=0:
        resultado=print(f"Seu ano {ano} é bissexto")
    elif ano1 == 0 and ano100 == 0 and ano400 == 0:
        resultado = print(f"Seu ano {ano} é bissexto")
    else:
        resultado=print(f"Seu ano {ano} não é bissexto")


    return resultado

pergunta=int(input("Digite o ano que você deseja saber"))

final=e_bissexto(pergunta)


#_____________________________________________________________________


## EXERCICIO 2 CONTAGEM DE CARACTERES  ##

def contar_caracteres(x,y):
    minha_string = x
    minuscula= minha_string.lower()

    resultado = print(f"A letra {y} se repete {minuscula.count(y)} vezes")

    return resultado


print(" Vamos contar as letrinhas?? ")
texto=str(input("\n Digite o eu texto:  "))
caractere_proc= str(input("Digite a letra procurada:  "))

final=contar_caracteres(texto,caractere_proc)

#__________________________________________________________________
# import random
# ## Simulador de Dado 

# def rolar_dado(lados):
#     aleatorio= random.randint(1,lados)

#     return aleatorio


# ataque=rolar_dado(20)
# dano=rolar_dado(8)

# print(f"Seu ataque é {ataque} e dano {dano}")