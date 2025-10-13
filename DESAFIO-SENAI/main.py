import cadastro_usuario

registro = {"usuario": "livro"}

print("==== MENU DE REGISTROS DE LIVROS ====")
usos = 3

print(input(f"Bem-vindo(a). Digite "))

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