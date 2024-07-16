from datetime import date, timedelta, time, datetime
import pandas as pd
import csv
from pathlib import Path

ROOTH_PATH = Path(__file__).parent
alunos_caminho = ROOTH_PATH / "alunos.csv"
professores_caminho = ROOTH_PATH / "professores.csv"

Domingos = []
alunos_df = pd.read_csv(alunos_caminho)
professores_df = pd.read_csv(professores_caminho)
print()
print("Bem vindo ao Sistema de gestão da Escola Biblica Dominical")

# user = input("Quem está acessando? ")
# print()

# password = input("Digite sua senha: " )
# print()

# print()
# print(f"Seja Bem Vindo {user.capitalize()} como posso ajudá-lo?")
# print()

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

def exibir_alunos():
    print(alunos_df)

def exibir_professores():
    print(professores_df)

def cadastrar_aluno():
    
    if alunos_caminho.exists():
        Alunos_df = pd.read_csv(alunos_caminho)
        ultima_matricula = int(Alunos_df['matricula'].iloc[-1])
        indice = ultima_matricula + 1
    
    nome = input("Digite o nome do aluno: ").capitalize()
    print(nome)
    sobrenome = input("Digite o sobrenome do aluno: " ).capitalize()
    print(sobrenome)
    for index, row in Alunos_df.iterrows():
        if nome.strip().lower() == row['nome'].strip().lower() and sobrenome.strip().lower() == row['sobrenome'].strip().lower():
            print(f"{nome} {sobrenome} já foi cadastrado")
            nome = input("Digite o nome do aluno: ").capitalize()
            sobrenome = input("Digite o sobrenome do aluno: " ).capitalize()
    else:
        data_de_nascimento = input("Digite a data de nascimento do aluno: # ex. 01.01.2002 : ")
        datas_formatadas = pd.to_datetime(data_de_nascimento, format='%d.%m.%Y')
        idade = 2024 - datas_formatadas.year
        sexo = input("digite o sexo do aluno. F para feminino e M para masculino: ").capitalize()
        telefone = str(input("digite o telefone do aluno: ex. 987871123 : "))
        classe = input("digite a classe do aluno: ").capitalize()
    
    with open(alunos_caminho, "a", encoding="utf-8", newline="") as arquivoAluno:
        escritorAluno = csv.writer(arquivoAluno)
        escritorAluno.writerow([indice, nome, sobrenome, idade, (data_de_nascimento.replace(".", "/")), sexo, telefone, classe])
        print(f"Aluno {nome} {sobrenome} cadastrado com sucesso")

def cadastrar_professor():
    
    if professores_caminho.exists():
        professores_df = pd.read_csv(professores_caminho)
        ultima_matricula = int(professores_df['matricula'].iloc[-1])
        indice = ultima_matricula + 1
    
    nome = input("digite o nome do professor: ").capitalize()
    sobrenome = input("digite o sobrenome do professor: ").capitalize()
    for index,row in professores_df.iterrows():
        if nome.strip().lower() == row["nome"].strip().lower() and sobrenome.strip().lower() == row["sobrenome"].strip().lower():
            print(f"{nome} {sobrenome} já cadastrado")
            nome = input("digite o nome do professor: ").capitalize()
            sobrenome = input("digite o sobrenome do professor: ").capitalize()
    else:
        data_de_nascimento = input("digite a data de nascimento do professor: ex. 01.01.2002 : ")
        data_formatada = pd.to_datetime(data_de_nascimento, format='%d.%m.%Y')
        idade = 2024 - data_formatada.year
        sexo = input("digite o sexo do professor. F para feminino e M para masculino : ").capitalize()
        telefone = str(input("digite o telefone do professor. ex. 987371023 : "))
        classe = input("digite a classe do professor: ").capitalize()
    
    with open(professores_caminho, "a", encoding="utf-8", newline="") as arquivoAluno:
        escritorProfessor = csv.writer(arquivoAluno)
        escritorProfessor.writerow([indice,  nome, sobrenome, idade,(data_de_nascimento.replace(".", "/")), sexo, telefone, classe])
        
        print(f"Professor {nome} {sobrenome} cadastrado com sucesso!!")
        
def acessar_aluno():
    Alunos_df = pd.read_csv(alunos_caminho)
    for index, row in Alunos_df.iterrows():
        print(f"{row['matricula']} - {row['nome']} {row['sobrenome']}")
    
    while True:
        nome_aluno_escolhido = input("Qual o nome do aluno deseja acessar? ")
        sobrenome_aluno_escolhido = input("Qual o sobrenome do aluno deseja acessar? ")
        
        # Procurar o aluno no dataframe
        aluno_encontrado = False
        for index, row in Alunos_df.iterrows():
            if (nome_aluno_escolhido.strip().lower() == row['nome'].strip().lower() and
                sobrenome_aluno_escolhido.strip().lower() == row['sobrenome'].strip().lower()):
                print()
                print(f"➖ Matricula: {row['matricula']}")
                print(f"➖ Nome: {row['nome']}")
                print(f"➖ Sobrenome: {row['sobrenome']}")
                print(f"➖ Idade: {row['idade']}")
                print(f"➖ Data de Nascimento: {row['data_de_nascimento']}")
                print(f"➖ Telefone: {row['telefone']}")
                print(f"➖ Sexo: {row['sexo']}")
                print(f"➖ Classe: {row['classe']}")
                aluno_encontrado = True
                break
        
        if aluno_encontrado:
            break
        else:
            print("Este aluno não está cadastrado, informe outro aluno.")

       
def acessar_professor():
    professores_df = pd.read_csv(professores_caminho)
    for index, row in professores_df.iterrows():
        print(f"{row['matricula']} - {row['nome']} {row['sobrenome']}")
    
    while True:
        nome_professor_escolhido = input("Qual o nome do aluno desejado? ")
        sobrenome_professor_escolhido = input("Qual o sobrenome do aluno desejado? ")

        aluno_encontrado = False
        for index, row in professores_df.iterrows():
            if nome_professor_escolhido.strip().lower() == row['nome'].strip().lower() and sobrenome_professor_escolhido.strip().lower() == row['sobrenome'].strip().lower():
                print()
                print(f"➖ Matricula: {row['matricula']}")
                print(f"➖ Nome: {row['nome']}")
                print(f"➖ Sobrenome: {row['sobrenome']}")
                print(f"➖ Idade: {row['idade']}")
                print(f"➖ Data de Nascimento: {row['data_de_nascimento']}")
                print(f"➖ Telefone: {row['telefone']}")
                print(f"➖ Sexo: {row['sexo']}")
                print(f"➖ Classe: {row['classe']}")
                aluno_encontrado = True
                break
        
        if aluno_encontrado:
            break
        else: 
            print("Este aluno não está cadastrado, informe outro aluno.")


# Chamada de funções
while True:
    print()
    funcao = input("O que deseja fazer? ")
    match funcao:
        case "1":
            print("Aguarde um instante...........")
            print()
            exibir_alunos()

        case "2":
            print("Aguarde um instante...........")
            print()
            exibir_professores()

        case "3":
            print("Aguarde um instante...........")
            print()
            cadastrar_aluno()

        case "4":
            print("Aguarde um instante...........")
            print()
            cadastrar_professor()
        
        case "5":
            print("Aguarde um instante...........")
            print()
            acessar_aluno()
        
        case "6":
            print("Aguarde um instante...........")
            print()
            acessar_professor()
        
        case "7":
            print("Aguarde um instante...........")
            print()
            # lista_de_domingos_do_trimestre()
        
        case "0":
            print("Volte sempre")
            break
