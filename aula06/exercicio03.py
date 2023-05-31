class atleta():

    def __init__(self, peso):
        self.peso = peso
        self.aquecer = False
        self.aposentar = False
        self.correr = False

    def aposentado(self):
        if self.aposentar == False:
            print(f' está aquecendo')
        self.aposentar =True
        else:
        print(f'o atleta ja está aposentado')

    def aquecer(self):
        if self.aquecer == False:
            print(f'é aposentado')
            self.aquecer = True

class corredor(atleta):

    def __init__(self):
        if self.aquecer == False:
            print(f'')
