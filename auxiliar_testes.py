import csv
from pathlib import Path
import pandas as pd
# import re

ROOT_PATH = Path(__file__).parent
alunos_caminho = ROOT_PATH / "alunos.csv"


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").capitalize()
    
    Alunos_df = pd.read_csv(alunos_caminho)
    if Alunos_df['matricula'].dropna().size > 0:
        indice = 1        
    else:
        ultima_matricula = int(Alunos_df['matricula'].iloc[-1])
        indice = ultima_matricula + 1

    with open(alunos_caminho, "a", encoding="utf-8", newline="") as arquivoAluno:
        escritorAluno = csv.writer(arquivoAluno)
        escritorAluno.writerow([indice, nome])
        print(f"Aluno {nome} cadastrado com sucesso")

cadastrar_aluno()