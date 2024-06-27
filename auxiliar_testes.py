from datetime import datetime, time, date, timedelta

Domingos = []

def lista_de_domingos_do_trimestre():
    ano_atual = datetime.now().year
    licao = int(input("Qual lição deseja acessar? "))
    mes_atual = datetime.now().month
    
    if mes_atual >= 1 and mes_atual <= 3:
        trimestre = 1
        
    elif mes_atual >= 4 and mes_atual <= 6:
        trimestre = 2
        
    elif mes_atual >= 7 and mes_atual <= 9:
        trimestre = 3
        
    else:
        trimestre = 4
    
    print(f" Estamos no {trimestre} º trimestre")

    trimestres = {
        1: (date(ano_atual, 1, 1), date(ano_atual, 3, 31)),
        2: (date(ano_atual, 4, 1), date(ano_atual, 6, 30)),
        3: (date(ano_atual, 7, 1), date(ano_atual, 9, 30)),
        4: (date(ano_atual, 10, 1), date(ano_atual, 12, 31))
    }
    if trimestre in trimestres:
        primeiro_dia, ultimo_dia = trimestres[trimestre]
        dias_do_mes = primeiro_dia
        
        while dias_do_mes <= ultimo_dia:
            if dias_do_mes.weekday() == 6:  # Verifica se é domingo
                Domingos.append(dias_do_mes)
            dias_do_mes += timedelta(days=1)
    else:
        print("Trimestre inválido. Por favor, escolha um valor entre 1 e 4.")
        
    for x in range(1,14):
        match licao:
            case x:
                print(f"acessando dados da {licao}º lição do dia {Domingos[x-1].strftime('%d/%m/%Y')}")
        break
    
lista_de_domingos_do_trimestre()