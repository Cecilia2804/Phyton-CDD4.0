class Conta:

    def __init__(self, conta, nomeCliente, tipo):
        self.nomeCliente = nomeCliente
        self.conta = conta
        self.saldo = 0
        self.status = False
        self.tipo = tipo
        self.limite = 0


    def depositar(self, valord):
        if self.status == True:
            print(f"O dinheiro foi depositado!")
            self.saldo = valord
        else:
            print(f'O dinheiro não foi depositado pois a conta está inativa!')
            self.status = False

    def sacar(self, valorS):
        if self.status == False:
            print(f"Não foi possível sacar o dinheiro pois a conta está inativa!")
        else:
            if valorS < self.saldo:
                print(f'seu dinheiro foi sacado!')
                self.saldo = self.saldo - valorS
            else:
                calculo = valorS - self.saldo
                self.limite = self.limite - calculo
                self.saldo = 0
                print(f'seu dinheiro foi sacado!')

    def verificarSaldo(self, ):
        if self.status == True:
            print(f'O saldo da conta é {self.saldo}!')
            self.status = True
        else:
            print(f'Não é possível ver o saldo pois a conta está inativa!')
            self.status = False

    def ativar(self, ):
        if self.status == False:
            print(f'A conta foi ativada!')
        else:
            print(f'Não foi possível ativar a conta pois a mesma ja está ativada!')
            self.status = True

    def desativar(self, ):
        if self.status == False:
            print(f'Não foi possível desativar a conta pois a mesma ja está desativada!')
            self.status = False
        else:
            if self.saldo != 0:
                print(f'Não foi possível desativar a conta pois é necessario que a conta esteja zerada!')
            else:
                print(f'A conta foi desativada!')
                self.status = False

    def A_limite(self,valorl):
        if self.ativar == True:
            print(f'limite ativado, seu limite é {valorl}')
            self.limite = valorl
        else:
            print(f'seu limite não foi ativado, pois sua conta não está ativa')
            self.limite = 0

    def D_limite(self,):
        if self.limite > 0:
            print(f'seu limite está inativo!')
            self.limite = 0
        else:
            print(f'seu limite está ativo!')

p2 = Conta(955280, "Mariane", "DACC")
p2.ativar()
p2.ativar()
p2.desativar()
p2.ativar()
p2.depositar(10)
p2.desativar()
p2.depositar(15)
p2.ativar()
p2.depositar(45)
p2.sacar(45)
p2.verificarSaldo()
p2.sacar(45)
p2.desativar()
p2.desativar()
