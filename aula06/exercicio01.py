#crie uma chamada ingresso, que possui um valor em reais e um metodo imprimirValor()
#crie uma class VIP, que herda de ingresso e possui um valor adicional.
#cire um metodo que retorne o valor do ingresso VIP(com o adicional incluido)
class ingresso():

    def __init__(self, valor):
        self.valor = valor
    def imprimirValor(self):
        print(self.valor)

class VIP(ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimirValor(self,adicional):
        print((self.valor * adicional / 100) + self.valor)

p2 = ingresso(50)
p2.imprimirValor()
p1 = VIP(50)
p1.imprimirValor(50)