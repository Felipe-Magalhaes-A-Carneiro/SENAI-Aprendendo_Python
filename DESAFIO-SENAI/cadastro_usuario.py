import main

novo_registro = {"usuario": "nome_usuario",
                 "livro": "nome_livro",
                 "avaliacao": "comentario"}

def cadastro():
    while True:
        print(f"""
            === CADASTRO DE LIVROS === 
            Digite uma das opções para prosseguir:

            1- Cadastrar livro
            2- Sair.
            """)
        escolha_cadastro = input("Escolher opção: ")
        
        if(escolha_cadastro == "1"):
            
            nome_usuario = input("Digite o nome de usuario:")
            novo_registro["usuario"] = nome_usuario

            nome_livro = input("Digite o nome do livro:")
            novo_registro["livro"] = nome_livro

            
            comentario = input("Faça um comentário sobre o livro:")
            novo_registro["avaliacao"] = comentario

            print("Registro realizado!")
            print(novo_registro)

        
        elif(escolha_cadastro == "2"):
            main()
    




