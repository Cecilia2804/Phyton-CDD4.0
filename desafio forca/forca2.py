import random

print('bem vindo ao jogo da forca! você tem ate 4 chances para acertar a palavra correta\n'
      'boa sorte!!!')
palavras = ['clavicula', 'clivagem', 'clorofila', 'cloroplastos', 'glandulas', 'globolos']

palavra_secreta = random.choices(palavras)
print(palavra_secreta)
print(f'a palavra escondida tem {len(palavra_secreta)} letras')
tentativas_certas = []
tentativas_erradas = []
erros = 0
while True:
    letra = input('digite uma letra: ').lower()
    if len(letra) == len(palavra_secreta):
        if letra == palavra_secreta:
            print("Parabéns, você acertou a palavra secreta:", palavra_secreta)
            break
        else:
            print('Você errou!, tente novamente')
            tentativas_erradas.append(letra)

            if letra in tentativas_certas or letra in tentativas_erradas:
                print('essa letra ja foi escolhida, escolha outra')
            elif letra in palavra_secreta:
                print('você acertou, continue!')
                letra.append(letra)
            else:
                print(f'errou! a palavra não contem a letra {letra}')
                erros += 1

            if erros == 4:
                print(f'GAME OVER. a palavra era {palavra_secreta}')

        tracos_da_forca = ['_'] * len(palavra_secreta)
        for item in palavra_secreta:
            if item in tentativas_certas:
                print(tracos_da_forca)

                if tracos_da_forca == palavra_secreta:
                    print('parabens!! você ganhou!')
                    break