##Crie um programa que ajude um pescador a controlar sua produtividade.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pel
#  regulamento (100 quilos), ele deve pagar uma multa de R$ 4,00 por quilo excedente.


#CONTROLE DE PRODUTIVIDADE


def quilos(x,a=100):
    "calcular o imposto gerado em caso da quantidade ser maior que 100 "
        
    (a-x)*4
   
for i in range(3):
    print(f"Vamos calcular os seus impostos {i+1} de 3 dias")
    quantidade=quilos(int(input("Digite a quantidade de peixes que você pescou no final de semana: ")))

    if quantidade >=100:
        print (f'Você pagará {quilos}')
    
    else:
        print("voce não pagara impostos")
    
   



