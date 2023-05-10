#crie um valor que recebe o nome de um PRODUTO, a QUANTIDADE que tem no estoque e o VALOR UNITARIO do produto
#retorne o valor total do meu estoque
def info(nome,q,valor):
    total = q * valor
    return nome, total
estoque = info("leite",5 , 10)
print(estoque)