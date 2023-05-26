#faça uma funçao que recebe um numero como parametro e verifique se este numero é primo
def primo(n):
    if n == 1:
        return n, "não é primo"
    elif n == 2:
        return n, "é primo"
    else:
        for x in range(2,n):
            if n % x == 0:
                return n, "não é primo"
            return n, "é primo"
