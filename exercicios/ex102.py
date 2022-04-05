def fatorial(n, show=False):
    """
    > Calcula o fatorial de N
    :param n:O número que você quer o fatorial
    :param show: Se quiser mostrar todo o cálculo deixar como True
    :return: O valor do fatorial do número
    """
    f = 1
    for c in range (n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f
print(fatorial(8, show=True))