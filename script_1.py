continuar = "s"

Alunos = [
    {"nome": "Miguel", "sobrenome": "Santos", "idade": "17", "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
    {"nome": "Robert", "sobrenome": "Santos", "idade": "22", "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
]

def exibir_alunos():
    print("Alunos cadastrados:")
    indice = 0
    for indice, aluno in enumerate(Alunos, start=1):
            print(f"{indice} - {aluno['nome']} {aluno['sobrenome']}")
    print()
    
def cadastrar_Aluno():
    while True:
        cadastrar_nome_aluno = str(input("Qual Aluno quer cadastrar? ")).strip()  
        cadastrar_sobrenome_aluno = str(input("Qual o sobrenome? ")).strip()  
        if cadastrar_nome_aluno:
            break
        print("nome do aluno não pode ficar em branco")
    
    while True:
        try:
            cadastrar_idade_aluno = int(input("Qual a idade deste aluno? "))    
            if cadastrar_idade_aluno > 0:
                break
            print("a idade deve ser um numero positivo, tente novamente")
        except ValueError:
            print("digite um numero valido para idade")
            
    cadastrar_sexo_aluno = str(input("Qual a sexo deste aluno? "))    
    cadastrar_telefone_aluno = str(input("Qual o telefone deste aluno? "))
    cadastrar_classe_aluno = str(input("Qual a classe deste aluno? "))
    
    novo_aluno = {
        "nome": cadastrar_nome_aluno.capitalize(),
        "sobrenome": cadastrar_sobrenome_aluno.capitalize(),
        "idade": cadastrar_idade_aluno,
        "sexo": cadastrar_sexo_aluno,
        "telefone": cadastrar_telefone_aluno,
        "classe": cadastrar_classe_aluno
    }
    
    Alunos.append(novo_aluno)
    print(f"Aluno: {cadastrar_nome_aluno} cadastrado com sucesso")
    print()




while continuar == "s":
    exibir_alunos() # mostrar todos os alunos
    cadastrar_Aluno() #cadastrar alunos
    exibir_alunos() #exibir depois do cadastro
    continuar = input("Deseja cadastrar mais alguem? responda 's' para sim, e 'n' para não: ")
else:
    print("Volte sempre")
    