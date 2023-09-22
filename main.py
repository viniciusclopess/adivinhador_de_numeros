import random
import os

#Limpar terminal
os.system('cls') 

#Gerar número entre 1 e 100 e contador de tentativas
numero_aleatorio = random.randint(1,100) 
contador_tentativas = 0

#Escolha do usuário
try:
    numero_escolhido = int(input('''Seja bem vindo ao adivinhador de números! 
Eu gerei um número aleatório e você deve acertar!
Escolha um número de 1 a 100: '''))
    tentativa_anterior = numero_escolhido
    contador_tentativas += 1

#O usuário só poderá errar o Value uma vez, se não o programa fecha
except ValueError: 
    try:
        numero_escolhido = int(input('''Apenas números inteiros! Tente novamente.
->'''))
    except ValueError:
        print('Encerrando programa...')
        exit()


#Loop para as tentativas até acertar o número gerado pelo computador
while True:
    if numero_escolhido > 100:
        try:
            numero_escolhido = int(input(f'''Apenas números entre 1 e 100! Tente novamente.
-> '''))
            tentativa_anterior = numero_escolhido
            contador_tentativas += 1
        except ValueError: 
            try:
                numero_escolhido = int(input('''Apenas números inteiros! Tente novamente.
->'''))
                tentativa_anterior = numero_escolhido
                contador_tentativas += 1
            except ValueError:
                print('Encerrando programa...')
                exit()
            

    elif numero_escolhido < numero_aleatorio:
        try:
            numero_escolhido = int(input(f'''Tente um número maior que {tentativa_anterior} 
-> '''))
            tentativa_anterior = numero_escolhido
            contador_tentativas += 1
        except ValueError:
            try:
                numero_escolhido = int(input('''Apenas números inteiros! Tente novamente.
->'''))
                tentativa_anterior = numero_escolhido
                contador_tentativas += 1
            except ValueError:
                print('Encerrando programa...')
                exit()
    
    elif numero_escolhido > numero_aleatorio:
        try:
            numero_escolhido = int(input(f'''Tente um número menor que {tentativa_anterior} 
-> '''))
            tentativa_anterior = numero_escolhido
            contador_tentativas += 1
        except ValueError:
            try:
                numero_escolhido = int(input('''Apenas números inteiros! Tente novamente.
->'''))
                tentativa_anterior = numero_escolhido
                contador_tentativas += 1
            except ValueError:
                print('Encerrando programa...')
                exit()

    #Acertou
    elif numero_escolhido == numero_aleatorio:
        print('--'*30)
        print(f'''Parabéns era o número {numero_aleatorio}! Você acertou em {contador_tentativas} tentativas! 
Deseja jogar novamente? 
[s] Sim
[n] Não''')
        escolha = input('->')
        while True:
            #Começar denovo
            if escolha == 's':
                os.system('cls')
                numero_aleatorio = random.randint(1,100)
                numero_escolhido = int(input("Novo número gerado! Escolha um número de 1 a 100: "))
                tentativa_anterior = numero_escolhido
                contador_tentativas = 0
                break
            #Encerrar jogo    
            elif escolha == 'n':
                print('Encerrando...')
                exit()
            else:
                escolha = input('''Resposta inválida, tente novamente.
-> ''')

    

