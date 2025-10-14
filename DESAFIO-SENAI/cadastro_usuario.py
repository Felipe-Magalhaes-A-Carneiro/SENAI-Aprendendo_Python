import registros

emprestimo = []

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
            return # Sai do loop de menu_cadastro e volta para main()
        else:
            opcao_usuario = input(cadastro_de_livros, "Escolha uma das opções: ") 


def cadastrar():

    while True:
        print("""
            ---> CADASTRAMENTO <---
            Digite o nome de usuario, o livro que foi emprestado e deixe uma avaliação dele sobre o livro. 
            
            ATENÇÃO: O cadastramento ocorre de forma continua, para parar digite 'sair', em usuário.
            """)

        nome_usuario = input("\nDigite o nome de usuario: ").title()
        
        if nome_usuario == 'sair': # Sai do loop de cadastrar e volta para menu_cadastro()
            return
        else:
            nome_livro = input("\nDigite o nome do livro: ").title()
            comentario = input(f"\nFaça um comentário do usuário sobre o livro '{nome_livro}': ")
            
            dicionario = {"usuario": nome_usuario, "livro": nome_livro, "avaliacao": comentario}
            emprestimo.append(dicionario)
            
            print("\n ---> Registro realizado!")

        registros.mostra_registros()
            
    



