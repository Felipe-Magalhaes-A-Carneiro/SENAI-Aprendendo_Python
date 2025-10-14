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
            return cadastrar()
        elif opcao_usuario == "2":
            return # retorna para função main()
        else:
            opcao_usuario = input(cadastro_de_livros, "Escolha uma das opções: ") 


def cadastrar():

    while True:
        print("""
            ---> CADASTRAMENTO <---
            Digite o nome de usuario, o livro que foi emprestado e deixe uma avaliação dele sobre o livro. 
            
            Se quiser sair, digite 'sair' em usuário.
            """)

        nome_usuario = input("\nDigite o nome de usuario: ")
        #permite sair para o menu de cadastro
        if nome_usuario == 'sair':
            return
        else:
            nome_livro = input("\nDigite o nome do livro: ")
            comentario = input(f"\nFaça um comentário do usuário sobre o livro '{nome_livro}': ")
            
            dicionario = {"usuario": nome_usuario, "livro": nome_livro, "avaliacao": comentario}
            emprestimo.append(dicionario)
            
            print("\n ---> Registro realizado!")

        print("\n --- REGISTROS ATUAIS ---")
        for cadastro in emprestimo:
                print(f"""
                Usuário: {cadastro['usuario']},
                Livro: {cadastro["livro"]},
                Avaliação: {cadastro["avaliacao"]}
                """)
            
    



