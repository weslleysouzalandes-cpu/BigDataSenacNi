for numero in range(5):
    try:
        print(f'numero {numero+1} de 5')
        num=float(input('digite um numero:'))


        dobro= num*2
        triplo= num*3
        quadruplo= num*4

        print(f'resultado: dobro={dobro}, triplo={triplo}, quadruplo={quadruplo}\n')
    except ValueError:
        print('entrada invalida. tente novamente.')
