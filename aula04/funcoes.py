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

def piramide(n):
    for x in range(1, 6):
        print(str(x)*x)
#piramide(5)

#faça um programa para imprimir uma priramide de 1 a 5
def piramide(a):
    for x in range(1, a+1):
        for y in range(1, x+1):
            print(y, end=" ")
        print()
#piramide(5)

def vogais(T):


    cont = 0
    for x in T:
        if x in 'aeiou':
            cont += 1
    #print(cont)
vogais(('o rato roeu a roupa do rei de roma'))

def info(nome,q,valor):
    total = q * valor
    return nome, total
estoque = info("leite",5 , 10)
#print(estoque)


  #  def lista(l):
        nova_lista = []
        for x in l:
            if x not in nova_lista:
                nova_lista.append(x)
       # print(nova_lista)

def num(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
               # print(number, 'não é primo')
                break
        else:
            print(number, 'é primo')
    elif number == 0:
        print(number, 'é zero')
    elif number == 1:
        print(number, 'não é primo')
    else:
       print(number, 'é negativo')


