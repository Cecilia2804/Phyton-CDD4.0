#fazer uma calculadora usando while
#1-somar/ 2-sub./3-multiplicar/4-dividir/5-sair
print("seja bem vindo!")
def somar(n1,n2):
    soma = n1 + n2
    print(soma)

def subtracao(n1, n2):
     sub = n1 - n2
     print(sub)
def multiplicacao(n1,n2):
    multi = n1 * n2
    print(multi)
def divisao(n1,n2):
    divi = n1 % n2
    print(divi)

opcao = 0
while True:
    print('1-somar'
          '2-sub.'
          '3-multiplicar'
          '4-dividir'
          '5-sair')
    opcao = int(input("selecione uma opção: "))
    if opcao == 1:
        n1 = int(input("digite o primeiro numero:"))
        n2 = int(input("digite o segundo numero:"))
        somar(n1,n2)
    elif opcao == 2 :
        n1 = int(input("digite o primeiro numero:"))
        n2 = int(input("digite o segundo numero:"))
        subtracao(n1,n2)
    elif opcao == 3:
        n1 = int(input("digite o primeiro numero:"))
        n2 = int(input("digite o segundo numero:"))
        multiplicacao (n1,n2)
    elif opcao == 4:
        n1 = int(input("digite o primeiro numero:"))
        n2 = int(input("digite o segundo numero:"))
        divisao(n1, n2)
    else:
        print("programa encerrado")
        break
