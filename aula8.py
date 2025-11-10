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

def calc_imc(peso,altura):

    imc= float(peso/altura*altura)
    
    return imc


def obter_classificacao(imc):
    if imc< 18.5:
        resultado = print(f'Seu imc é {imc}, você está abaixo do peso')
    elif 18.5<=imc<=24.9:
        resultado = print(f"Peso normal")
    elif 25.0<=imc<=29.9:
        resultado=(f"Você está com Sobrepeso")
    else:
        resultado = print("Obesidade")
    
    return resultado




total_de_pessoas=int(input('Quantas pessoas precisam calcular seu IMC??  '))

for i in range(total_de_pessoas):
    print(f"Você está calculando {i+1} de {total_de_pessoas}")
    

    
    peso=int(input('Digite o peso desta pessoa:  '))
    altura=int(input('Digite a altura desta pessoa em centímetros: '))


imc_impresso= calc_imc(peso,altura)
classificacao= obter_classificacao(imc_impresso)

print(f"O seu imc é {imc_impresso} e sua classificacao é {classificacao} ")