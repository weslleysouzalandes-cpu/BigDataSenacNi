# for numero in range(5):
#     try:
#         print(f'numero {numero+1} de 5')
#         num=float(input('digite um numero:'))


#         dobro= num*2
#         triplo= num*3
#         quadruplo= num*4

#         print(f'resultado: dobro={dobro}, triplo={triplo}, quadruplo={quadruplo}\n')
#     except ValueError:
#         print('entrada invalida. tente novamente.')


## EXERCÍCIO 1

#Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora 
# para 10 estudantes.

resultadofinal=[]
for i in range(5):
    print(f'Numero {i+1} de 10')

    try:
        print('Bem vindo à calculadora de notas! Primeiro, digite suas duas primeiras notas')

        notaum=float(input('Digite a sua primeira nota:  '))

        n_2=float(input('Digite a sua segunda nota:  '))
    

        media= float((notaum+n_2)/2)
    

        if media >=6.0:
            print('PARABÉNS! VOCÊ ESTÁ APROVADO!!')
        
        elif media<3.0:
            print(f'Sinto muito, você está reprovado. Sua média é {media}')
        else:
            nota3=float(input('Vejo que você ficou de recuperação, por favor, digite a sua terceira nota. Caso não tenha feito, digite -1: '))
            if nota3 ==-1:
                print(f'Sinto muito, você está reprovado. Sua nota é: {media}')
            else:

                if nota3 > notaum or nota3>n_2 and notaum > n_2:
                        situacao=float((nota3+notaum)/2)
                        if situacao>=6.0:
                                print(f'Parabéns, você está aprovado" Sua nota final é {situacao}')
                        else:
                                print('Sinto muito, você está reprovado')
                elif nota3 > n_2 or nota3 > notaum and n_2 > notaum:
                    
                    situacao=float((nota3+n_2)/2)
                    if final>=6.0:
                        print (f'Parabéns, você está aprovado! Sua nota final é {situacao}')
                    else:
                        print(f'Sinto muito, você está reprovado, sua nota final é {situacao}')
                elif n_2==notaum and nota3>notaum or nota3>n_2:
                    situacao=float((nota3+notaum)/2)
                    print(f'sua nota final é {situacao}')
                else:
                    print(f'Sua média final é {media}')
        
        resultadofinal=resultadofinal.append(situacao)

    except ValueError:
     print('Digite um número para calcular')

print(f'resultado final: {resultadofinal}')

## EXERCÍCIO 2

# for i in range(12):
#     print(f'Candidato {i+1} de 12')

#     try:
#         print('Primeiro, diga qual seu ano de nascimento')
#         idade=int(input('Por favor, digite o seu ano de nascimento: '))
#         ano=2025
#         diferenca=int(ano-idade)

#         if diferenca < 18:
#             print(f'Você não pode participar do programa, sua idade é {diferenca} anos')
#             break
              
              
#         elif diferenca >= 18:
#             x=str(input('Digite seu nome completo:  '))
#             y=str(input('Digite seu cpf completo:  '))
#             z=str(input('Digite seu endereço completo:  '))

#             print(f'parabéns,{x} você está cadastrado')
#         else:
#             print('DIGITE UM VALOR CORRETAMENTE')

#     except ValueError:
#         print('Digite o ano corretamente')


## EXERCÍCIO 3
# 
# TENTATIVA DE LOGIN






# for i in range(3):
#     print(f'Tentativa {i+1} de 3 ')
#     usuario='admin'
#     senha=123

#     try:
#         xx=str(input('Digite o seu nome de usuário:  '))
#         yy=str(input('Dgite a sua senha:'))

#         if xx == usuario and yy == senha:
#             print('Seja bem vindo')
#             break
#         elif yy!= senha:
#             print('A senha ou usuario está errada, tente novamente')
#             print(f'Tentativa {i+1} de 3 ')  

        
#         else:            
#             print('Senha e admin errados')
        
#         match i:
#             case 2:
#                 print('Número de tentativas esgotadas, o sistema está bloqueado')


#     except ValueError:
#         print('digite corretamente')
# #         





# usuario=admin
# senha=123456
# tentativas=3
# contador=0
# while contador < tentativas:
#     try:
#         print(f'tentativas: {contador+1} de {tentativas}')

#         input_usuario=input('Digite seu login: ')
#         input_senha= int(input('Digite sua senha: '))

#         if usuario == input_usuario and senha==input_senha:
#             print('Sucesso" Login efetuado. Bem vindo(a) ')
#         else:
#             print('Usuário ou senha inválidos. Tente novamente.')
#             tentativas -=1
#             contador+=1
#             print(f'tentativas: {contador+1} de {tentativas}')
            



    
#     except ValueError:
#         print('ERRO: dados invalidos')
#  if tentativas==0:
#     print('Sistema boqueado')

 