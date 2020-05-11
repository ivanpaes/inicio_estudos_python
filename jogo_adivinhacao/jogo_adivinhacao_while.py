import numpy as np

print('================================')
print('Bem vindo ao jogo de adivinhação')
print('================================')

numero_secreto = np.random.randint(1,50)
rodada = 1
total_tentativas = 10

print('Eu pensei em um número entre 1 e 50. Tente adivinha-lo!')

while rodada <= total_tentativas:
    print('Tentativa {} de {}'.format(rodada, total_tentativas))
    chute = int(input('Digite seu número: '))
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    rodada += 1

    if(chute < 1 or chute > 50):
        print('Por favor, apenas números entre 1 e 50')
        continue

    if(acertou):
        print('Parabéns! Você acertou.')
        break

    else:
        if(menor):
            print('Lamento, você errou! Seu chute foi menor que o número secreto')
        elif(maior):
            print('Lamento, você errou! Seu chute foi maior que o número secreto')
    
print('FIM DO JOGO')