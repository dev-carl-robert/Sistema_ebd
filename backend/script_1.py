from datetime import date, timedelta, time, datetime

    # Listas
Alunos = [
    {"nome": "Miguel", "sobrenome": "Santos", "idade": 17, "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
    {"nome": "Robert", "sobrenome": "Santos", "idade": 22, "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
]

Professores = [
    {"nome": "Roberto", "sobrenome": "Ferreira", "idade": 48, "sexo": "masculino", "telefone": "9####-####", "classe": "adultos"},
    {"nome": "Cleude", "sobrenome": "Santos", "idade": 43, "sexo": "feminino", "telefone": "9####-####", "classe": "Jardim"},
]

Domingos = []

    # Fim das Listas
print()
print("Bem vindo ao Sistema de gestão da Escola Biblica Dominical")

user = input("Quem está acessando? ")
print()

password = input("Digite sua senha: " )
print()

print()
print(f"Seja Bem Vindo {user.capitalize()} como posso ajudá-lo?")
print()
    
    
def menu():
    print("""
    | -----------------------------------------|
    | exibir tabela de alunos = digite 1       |
    | exibir tabela de professores = digite 2  |
    | cadastrar aluno = digite 3               |
    | cadastrar professor = digite 4           |
    | Acessar aluno = digite 5                 |
    | Acessar professor = digite 6             |
    | Lista de presença = 7                    |
    | encerrar ação = digite 0                 |
    | _________________________________________|
    """)
menu()

    # Funções
def exibir_alunos():
    print("Alunos cadastrados: ")
    for indice, aluno in enumerate(Alunos, start=1):
        print(f"{indice} - {aluno['nome']} {aluno['sobrenome']}")
    print()

def exibir_professores():
    print("Professores cadastrados: ")
    for indice, professor in enumerate(Professores, start=1):
        print(f"{indice} - {professor['nome']} {professor['sobrenome']}")
    print()

def cadastrar_pessoa(tipo):
    while True:
        nome = str(input(f"Qual {tipo} quer cadastrar? ")).strip()
        sobrenome = str(input("Qual o sobrenome? ")).strip()
        if nome:
            break
        print(f"####Nome do {tipo} não pode ficar em branco#####")

    while True:
        try:
            idade = int(input(f"Qual a idade deste {tipo}? "))
            if idade > 0:
                break
            print("#####A idade deve ser um número positivo, tente novamente#####")
        except ValueError:
            print("#####Digite um número válido para idade#####")

    sexo = str(input(f"Qual o sexo deste {tipo}? "))
    telefone = str(input(f"Qual o telefone deste {tipo}? "))
    classe = str(input(f"Qual a classe deste {tipo}? "))

    nova_pessoa = {
        "nome": nome.capitalize(),
        "sobrenome": sobrenome.capitalize(),
        "idade": idade,
        "sexo": sexo,
        "telefone": telefone,
        "classe": classe
    }

    return nova_pessoa

def cadastrar_aluno():
    aluno = cadastrar_pessoa("aluno")
    Alunos.append(aluno)
    print(f"Aluno {aluno['nome']} cadastrado com sucesso")

def cadastrar_professor():
    professor = cadastrar_pessoa("professor")
    Professores.append(professor)
    print(f"Professor {professor['nome']} cadastrado com sucesso")

def acessar_aluno():
    print('escolha o numero do aluno desejado')
    exibir_alunos()
    aluno_escolhido = int(input("Qual aluno deseja acessar? "))
    aluno_acessado = Alunos[aluno_escolhido - 1]
    print(30 * "_")
    print(f"Nome Completo: {aluno_acessado['nome']} {aluno_acessado['sobrenome']}")
    print(f"Idade: {aluno_acessado['idade']}")
    print(f"Sexo: {aluno_acessado['sexo']}")
    print(f"Telefone: {aluno_acessado['telefone']}")
    print(f"Classe: {aluno_acessado['classe']}")
    print(30 * "_")    

def acessar_professor():
    
    print("Escolha o professor desejado")
    exibir_professores()
    professor_escolhido = int(input("Qual professor deseja acessar? "))
    professor_acessado = Professores[professor_escolhido - 1]
    print(30 * "_")
    print(f"Nome Completo: {professor_acessado['nome']} {professor_acessado['sobrenome']}")
    print(f"Idade: {professor_acessado['idade']}")
    print(f"Sexo: {professor_acessado['sexo']}")
    print(f"Telefone: {professor_acessado['telefone']}")
    print(f"Classe: {professor_acessado['classe']}")
    print(30 * "_")    
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
                print()
                print(f"acessando dados da {licao}º lição do dia {Domingos[x-1].strftime('%d/%m/%Y')} do {trimestre} º trimestre")
        break

    # Fim das Funções

# Chamada de funções
while True:
    print()
    funcao = input("O que deseja fazer? ")
    match funcao:
        case "1":
            print("Aguarde um instante...........")
            exibir_alunos()

        case "2":
            print("Aguarde um instante...........")
            exibir_professores()

        case "3":
            print("Aguarde um instante...........")
            cadastrar_aluno()

        case "4":
            print("Aguarde um instante...........")
            cadastrar_professor()
        
        case "5":
            print("Aguarde um instante...........")
            acessar_aluno()
        
        case "6":
            print("Aguarde um instante...........")
            acessar_professor()
        
        case "7":
            print("Aguarde um instante...........")
            lista_de_domingos_do_trimestre()
        
        case "0":
            print("Volte sempre")
            break
