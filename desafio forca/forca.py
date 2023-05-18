import random

palavras = ['cloroplastos', 'clorofila', 'clavicula', 'clivagem']
escolhas = random.choice(palavras)
print(escolhas)
tentativas = 0
chances = 5
letras_escolhidas = []
estado_atual = ['_'] * len(palavras)

print('\nbem vindo ao jogo da forca!'
      'escolhas as letras e tente acertar as frases, divirtasse!!')

while tentativas <= chances and ''.join(estado_atual) != escolhas:

 letra = input('qual letra você escolhe ?')

    if letra in letras_escolhidas:
        print('você ja escolheu essa letra, escolha outra')
        letras_escolhidas.append(letra)
        if letra in escolhas:
            for i in range(len(escolhas)):
                if letra == escolhas[i]:
                    estado_atual[i] = letra
            print('parabens! voê acertou, continue')
        else:
            print('você errou! restam', chances, 'chances')
            tentativas += 1
        #quantas tentativas ele tem
            print('você ja fez', tentativas, 'restam ', chances - tentativas, 'tentativas')

        #letras certas da palavra
            print('esse é o estado atual: ', estado_atual)


         #quais letras ja tentou
            print('as letras que você ja tentou sao: ', letras_escolhidas)
            for x in letras_escolhidas:
                print(x, end=" ")

            #fazer um final pro jogo
                if tentativas == chances:
                    print('acabaram suas tentativas! GAME OVER')
                else:
                    print('você conseguiu! a palavra era', escolhas)
