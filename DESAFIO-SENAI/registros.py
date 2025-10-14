import cadastro_usuario

def mostra_registros():
    
    print("\n --- REGISTROS ATUAIS ---")
    for cadastro in cadastro_usuario.emprestimo:
        print(f"""
        Usuário: {cadastro['usuario']},
        Livro: {cadastro["livro"]},
        Avaliação: {cadastro["avaliacao"]}
        """)