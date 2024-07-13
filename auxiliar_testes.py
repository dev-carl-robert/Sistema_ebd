import csv
from pathlib import Path
import pandas as pd
# import re

ROOT_PATH = Path(__file__).parent
caminho_csv = ROOT_PATH / "alunos.csv"


nome = input("Qual o nome do aluno? ")
sobrenome = input("Qual o sobrenome do aluno? ")
data_de_nascimento = input("Qual a data de nascimento do aluno? ex: 01.01.2002 : ")
datas_formatadas = pd.to_datetime(data_de_nascimento, format='%d.%m.%Y')
idade = 2024 - datas_formatadas.year
sexo = input("Qual o sexo do aluno? ")
telefone = str(input("Qual o telefone do aluno? ex: 987112233 : "))
classe = input("Qual a classe do aluno? ")

if caminho_csv.exists():
    Alunos_df = pd.read_csv(caminho_csv)
    ultima_matricula = int(Alunos_df['matricula'].iloc[-1])
    indice = ultima_matricula + 1

    
with open(caminho_csv, "a", encoding="utf-8", newline="") as arquivoAluno:
    escritorAluno = csv.writer(arquivoAluno)
    escritorAluno.writerow([indice, nome, sobrenome, idade, (data_de_nascimento.replace(".", "/")), sexo, telefone, classe])

print(Alunos_df)

# excluir
# Alunos_df = Alunos_df[Alunos_df['nome'] != 'mariana']
# Alunos_df.to_csv(caminho_csv, index=False, encoding='utf-8')


# for row in Alunos_df:
#     print(row)
