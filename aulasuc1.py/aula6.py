##listas, Tuplas, Sets e Dicionários

# lista01=['Douglas',30,30.4,True,None,'Maria', {1,2,3}, {'nome': 'joao'},(30,40,50),[2,4,6,8]]
# print(lista01)
# print(type(lista01))
# print(lista01[2])



# lista_alunos=[]
# lista_alunos.append=('media')

# print(lista_alunos)

#--------------------------------------------------------------------------------------------------------

#Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
# (if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
# string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().

# lista=[]
# try:
#     for i in range(2):
#         print(f' Nota calculada {i+1} de 2')
        


#         print('Bem vindo a calculadora de notas')
#         z=str(input('Digite o seu nome: '))
#         x=float(input('Digite a sua primeira nota:  '))
#         y=float(input('Digite a sua segunda nota:  '))

#         media=float((x+y)/2)
#         print(f'A sua média é {media}')

#         if media>=6:
                
#             print(lista.append(f'aluno {z} - aprovado com media {media}'))
        
#         else:
#             print(lista.append(f'aluno {z} - reprovado com media {media}'))
# except ValueError:
#     print('Digite um valor possível de ser calculado')
        
    
# print(lista)

#___________________________________________________________________________________________
## EXERCÍCIO 2

##Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato)



lista=[]
try:          

    for i in range(2):
        print(f'Candidato {i+1} de 2')


        
        idade=int(input('Digite a seu ano de nascimento:  '))
        

        x=int(2025-idade)

        if x<18:
            print('Vejo que você não é maior de idade, por isso, não poderá participar')

        elif x>=18:
            print(f'vejo que você possui {x} anos, parabéns você está apto')
            nome=str(input('Por favor, digite o seu nome:  '))
            email=str(input('Digite o seu email: '))
            endereco=str(input('Digite o seu endereco: '))
            candidato={"nome": nome , 
                "endereco": endereco,
                "idade": idade,
                "email": email}
        else:
            print('digite algo válido')

        
        lista.append(candidato)
            
    print('*'*30)
except ValueError:
    print('digite algo valido')

print(lista)
