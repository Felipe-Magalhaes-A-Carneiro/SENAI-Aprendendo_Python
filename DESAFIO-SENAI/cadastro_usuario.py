import main

registro = [
    {"usuario": "nome_usuario",
     "livro": "nome_livro",
     "avaliacao": "comentario"}]

def menu_cadastro():
    while True:

        print(f"""
            === CADASTRO DE LIVROS === 
            Digite uma das opções para prosseguir:

            1- Cadastrar livro
            2- Sair.
            """)
        opcao_usuario = input("Escolha uma das opções: ")
        if opcao_usuario == "1":
            return cadastrar()
        else:
            return main()


def cadastrar():

    while True:

        escolha_cadastro = input("Escolher opção: ")
        
        if(escolha_cadastro == "1"):
            print("\nCadastramento - Digite o nome de usuario, o livro que foi emprestado e deixe um comentário dele sobre o livro. \nSe quiser sair, digite 'sair' em usuario.")

            nome_usuario = input("Digite o nome de usuario:")
            #permite sair para o menu de cadastro
            if nome_usuario == 'sair':
                return menu_cadastro()
            else:
                nome_livro = input("Digite o nome do livro:")
                comentario = input(f"Faça um comentário sobre o livro '{nome_livro}':")
            
            cadastro = {"usuario": nome_usuario, "livro": nome_livro, "avaliacao": comentario}
            registro.append(cadastro)
            
            print("Registro realizado!")
            print(cadastro)
            print(registro)
    




