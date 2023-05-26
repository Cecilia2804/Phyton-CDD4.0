class animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'o {self.nome} foi comer...')
    def Emitirsom(self):
        print(f' {self.nome} está emitindo som...')

class gato(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Emitirsom(self):
        print(f'o {self.nome} foi miando...')

class cachorro(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Emitirsom(self):
        print(f'o {self.nome} aprendeu a latir')

class vaca(animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

p2 = vaca('a lari', 'marrom')
p2.Emitirsom()

