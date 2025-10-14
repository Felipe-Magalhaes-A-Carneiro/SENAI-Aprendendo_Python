import cadastro_usuario

print("""\n==== PROGRAMA DE REGISTROS DE LIVROS ====\n""")

inicializar = input(f"Bem-vindo(a). \nDigite 'y' para continuar: ")

def main():
    while True:

        print(f"""
            ==== MENU DE REGISTROS DE LIVROS ====
                     
            Digite uma das opções abaixo:
                     
            1- Cadastrar um novo emprestimo de livros;
            2- Análizar os livros já cadastrados;
            3- Sair do programa.
            """)
        escolha_menu= input("Escolher opção: ")
        
        if escolha_menu == "1":
            cadastro_usuario.menu_cadastro()

        elif escolha_menu == "2":
            print("*Mostra todos os registros*")
            main()

        elif escolha_menu == "3":
            print("Saindo do programa. Obrigado e volte sempre!")
            break

if inicializar == 'y':
    main() 