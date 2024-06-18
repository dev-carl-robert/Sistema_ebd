continuar = "s"
Alunos = [
        {"nome": "Miguel", "sobrenome": "Santos", "idade": "17", "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
        {"nome": "Robert", "sobrenome": "Santos", "idade": "22", "sexo": "masculino", "telefone": "9####-####", "classe": "jovens"},
    ]

Professores = [
        {"nome": "Roberto", "sobrenome": "Ferreira", "idade": "48", "sexo": "masculino", "telefone": "9####-####", "classe": "adultos"},
        {"nome": "Cleude", "sobrenome": "Santos", "idade": "42", "sexo": "feminino", "telefone": "9####-####", "classe": "Jardim"},
    ]    
    
print( """
| -----------------------------------------|    
| exibir tabela de alunos = digite 1       |
| exibir tabela de professores = digite 2  |
| cadastrar aluno = digite 3               |
| cadastrar professor = digite 4           |
| encerrar ação = digite 0                 |
| _________________________________________|      
    """)

while continuar=="s":
    funcao = input("O que deseja fazer? ")

    def exibir_alunos(): 
        print("Alunos cadastrados: ")
        indice = 0
        for indice, aluno in enumerate(Alunos, start=1):
                print(f"{indice} - {aluno['nome']} {aluno['sobrenome']}")
        print()

    def exibir_Professores():
        print("Professores cadastrados: ")
        indice = 0
        for indice, professor in enumerate(Professores, start=1):
                print(f"{indice} - {professor['nome']} {professor['sobrenome']}")
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
        print("Alunos cadastrados: ")
        indice = 0
        for indice, aluno in enumerate(Alunos, start=1):
                print(f"{indice} - {aluno['nome']} {aluno['sobrenome']}")
        print()

        print()
        
    def cadastrar_Professores():
        while True:
            cadastrar_nome_professor = str(input("Qual Professor quer cadastrar? ")).strip()  
            cadastrar_sobrenome_professor = str(input("Qual o sobrenome? ")).strip()  
            if cadastrar_nome_professor:
                break
            print("nome do professor não pode ficar em branco")
        
        while True:
            try:
                cadastrar_idade_professor = int(input("Qual a idade deste professor? "))    
                if cadastrar_idade_professor > 0:
                    break
                print("a idade deve ser um numero positivo, tente novamente")
            except ValueError:
                print("digite um numero valido para idade")
                
        cadastrar_sexo_professor = str(input("Qual a sexo deste professor? "))    
        cadastrar_telefone_professor = str(input("Qual o telefone deste professor? "))
        cadastrar_classe_professor = str(input("Qual a classe deste professor? "))
        
        novo_professor = {
            "nome": cadastrar_nome_professor.capitalize(),
            "sobrenome": cadastrar_sobrenome_professor.capitalize(),
            "idade": cadastrar_idade_professor,
            "sexo": cadastrar_sexo_professor,
            "telefone": cadastrar_telefone_professor,
            "classe": cadastrar_classe_professor
        }
        
        Professores.append(novo_professor)
        print(f"professor: {cadastrar_nome_professor} cadastrado com sucesso")
        print("Professores cadastrados: ")
        indice = 0
        for indice, professor in enumerate(Alunos, start=1):
                print(f"{indice} - {professor['nome']} {professor['sobrenome']}")
        print()

    match funcao:
        case "1":
            exibir_alunos()
        case "2":
            exibir_Professores()
        case "3":
            cadastrar_Aluno()
        case "4":
            cadastrar_Professores()
        case "0":
            print("Volte sempre")
            break