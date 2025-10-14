import cadastro_usuario

print("""\n==== PROGRAMA DE REGISTROS DE LIVROS ====\n""")
usos = 3

inicializar = input(f"Bem-vindo(a). \nDigite 'y' para continuar: ")

def main():
    while usos != 0:
        print(f"""
            ==== MENU DE REGISTROS ====
                     
            Digite uma das opções abaixo:
                     
            1- Cadastrar registro de livros;
            2- Análizar os livros já cadastrados;
            3- Sair
            """)
        escolha_menu= input("Escolher opção: ")
        
        if escolha_menu == 1:
            cadastro_usuario()

        elif escolha_menu == 3:
            print("Saindo do programa. Obrigado e volte sempre!")
            break
        usos -= 1

if inicializar == 'y':
    main()