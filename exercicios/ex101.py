def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos ainda não vota!'
    elif 16 <= idade < 18 or idade >= 60:
        return f'Com {idade} anos o voto é opcional!'
    else:
        return f'VOTO OBRIGATÓRIO!'

nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))