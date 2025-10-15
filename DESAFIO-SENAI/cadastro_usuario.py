import registros

emprestimo = []

def cadastrar():

    while True:
        print("""
            ---> CADASTRAMENTO <---
            Digite o nome de usuario, o livro que foi emprestado e deixe uma avaliação dele sobre o livro. 
            
            ATENÇÃO: O cadastramento ocorre de forma continua, para parar digite ' 0 '(zero), em usuário.
            """)

        nome_usuario = input("\nDigite o nome de usuario: ").title()
        
        if nome_usuario == '0': # Sai do loop de cadastrar e volta para menu_cadastro()
            break
        else:
            nome_livro = input("\nDigite o nome do livro: ").title()
            comentario = input(f"\nFaça um comentário do usuário sobre o livro '{nome_livro}': ")
            
            dicionario = {"usuario": nome_usuario, "livro": nome_livro, "avaliacao": comentario}
            emprestimo.append(dicionario)
            
            print("\n ---> Registro realizado!")

        registros.mostra_registros()

def menu_cadastro():
    while True:

        cadastro_de_livros = print(f"""
            === CADASTRO DE LIVROS === 
            Digite uma das opções para prosseguir:

            1- Cadastrar livro
            2- Sair.
            """)
        opcao_usuario = input("Escolha uma das opções: ")

        if opcao_usuario == "1":
            cadastrar()
        elif opcao_usuario == "2":
            return 
        else:
            opcao_usuario = input(cadastro_de_livros, "Escolha uma das opções: ") 
            
    



