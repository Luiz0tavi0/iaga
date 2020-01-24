from datetime import date

def primeiro_util(mes):
    for d in range(1,4):
        dia = date(date.today().year,mes,d)
        if dia.weekday() not in (5,6):
            return dia

def proximo_util(dia_x, qtd= 1):
        return dia_x.fromordinal(dia_x.toordinal() + qtd)

def dias_uteis(mes = date.today().month):    
    dia_atual= primeiro_util(mes) #primeiro útil dia do mês

    while dia_atual.month == mes:        
        if dia_atual.weekday() == 5:
            dia_atual= proximo_util(dia_atual,1)
        else:
            yield dia_atual
        dia_atual= proximo_util(dia_atual,1)

