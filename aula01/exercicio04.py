#faça uma funçao que conte quantaas vogais tem num texto
#texto: o rato roeu a roupa do rei de roma
def vogais(T):


    cont = 0
    for x in T:
        if x in 'aeiou':
            cont += 1
    print(cont)
vogais(('o rato roeu a roupa do rei de roma'))




