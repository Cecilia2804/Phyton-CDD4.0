#faça um programa para imprimir uma priramide de 1 a 5
def piramide(a):
    for x in range(1, a+1):
        for y in range(1, x+1):
            print(y, end=" ")
        print()
piramide(5)

