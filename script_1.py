Alunos = [
    {"nome": "Miguel", "idade": 17, "sexo": "masculino", "telefone": "9####-####"},
    {"nome": "Apolo", "idade": 17, "sexo": "masculino", "telefone": "9####-####"},
    {"nome": "Silas", "idade": 15, "sexo": "masculino", "telefone": "9####-####"}
]
def exibir_alunos():
    print("tabela atual")
    for aluno in Alunos:
        for chave, valor in aluno.items():
            print(f"{chave} : {valor}")
        print() 

def cadastrar_Aluno():
    while True:
        cadastrar_nome_aluno = str(input("Qual Aluno quer cadastrar? ")).strip()  
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
    
    novo_aluno = {
        "nome": cadastrar_nome_aluno,
        "idade": cadastrar_idade_aluno,
        "sexo": cadastrar_sexo_aluno,
        "telefone": cadastrar_telefone_aluno,
    }
    
    Alunos.append(novo_aluno)
    print(f"Aluno: {cadastrar_nome_aluno} cadastrado com sucesso")

exibir_alunos() #exibir antes do cadastro
cadastrar_Aluno() #cadastrar alunos
exibir_alunos() #exibir depois do cadastro

    