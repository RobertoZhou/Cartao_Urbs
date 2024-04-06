verificar_registro = 0
while verificar_registro < 4:
    if(verificar_registro == 0):
        print("=====================================")
        print("         REGISTRAR CLIENTE")
        print("=====================================")
        usuario_nome = input("Digite Seu Nome de Usúario: ")
        if(usuario_nome != "" and usuario_nome != " "):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo com seu Nome!!!")
    if(verificar_registro == 1):
        usuario_senha = input("Digite Sua Senha: ")
        if(usuario_senha != "" and usuario_senha != " "):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo Com Sua Senha!!!")

    if(verificar_registro == 2):
        print("=====================================")
        print("      REGISTRAR ADMINISTRADOR")
        print("=====================================")
        admin_nome = input("Digite Seu Nome: ")
        if(admin_nome != "" and admin_nome != " "):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo com seu Nome!!!")
    if(verificar_registro == 3):
        admin_senha = input("Digite Sua Senha: ")
        if(admin_senha != "" and admin_senha != " "):
            verificar_registro = verificar_registro + 1
            preco_passagem = float(input("Por Favor, Digite o Valor da Passagem: R$"))
        else:
            print("Por Favor, Preencha o Campo Com Sua Senha!!!")

opcao = 0
saldo_credito = 0
while opcao != 3:
    print("=====================================")
    print("                 MENU")
    print("=====================================")
    print("1 - Cliente.")
    print("2 - Administrador.")
    print("3 - Encerrar Sessão.")
    print("=====================================")
    print("Por Favor, Escolha entre [ 1, 2 e 3 ]")
    opcao = int(input("Qual Usuário acima você é: "))
    print("=====================================")

    if(opcao == 1):
        #   Login Cliente
        tentativa = 4
        while tentativa > 0:
            print("            LOGIN CLIENTE")
            print("=====================================")
            login_nome_usuario = input("Digite o Nome de Usuário: ")
            login_senha_usuario = input("Digite a Senha de Usuário: ")
            print("=====================================")
            if(login_nome_usuario == usuario_nome and login_senha_usuario == usuario_senha):
                tentativa = 0
            else:
                print("Nome ou Senha Invalida!!!")
                tentativa = tentativa - 1
                print("Tentativas Restantes:", tentativa, "Tentativa")
                print("=====================================")
                if(tentativa == 0):
                    print("Voltando Para o Menu!!!")
        #   Menu Cliente
        if(login_nome_usuario == usuario_nome and login_senha_usuario == usuario_senha):
            while opcao != 5:
                print("=====================================")
                print("             MENU CLIENTE")
                print("=====================================")
                print("1 - Visualizar Créditos.")
                print("2 - Depositar Crédito.")
                print("3 - Utilizar o Cartão.")
                print("4 - Atualizar Senha.")
                print("5 - ENCERRANDO SESSÃO.")
                print("=====================================")
                print("Por Favor, Escolha entre [ 1, 2, 3, 4 e 5 ]")
                opcao = int(input("Digite a Sua Opção:"))
                print("=====================================")
                #   Visualizar Créditos
                if(opcao == 1):
                    print("O Cliente:", usuario_nome)
                    print("Créditos Possuído: R$", saldo_credito)

                #   Depositar Crédito
                elif(opcao == 2):
                        print("=====================================")
                        print("O Cliente:", usuario_nome)
                        print("Créditos Possuído: R$", saldo_credito)
                        print("Valor da Passagem: R$", preco_passagem)
                        print("=====================================")
                        deposito_credito = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                        print("=====================================")
                        saldo_credito = saldo_credito + deposito_credito
                        print("Saldo Atual: R$", saldo_credito)
                #   Utilizar o Cartão
                elif(opcao == 3):
                    if(saldo_credito >= preco_passagem):
                        print("Preço da Passagem: R$", preco_passagem)
                        print("PASSAGEM PASSADO COM SUCESSO!!!")
                        print("Boa-Viagem,", usuario_nome)
                        saldo_credito = saldo_credito - preco_passagem
                        print("Saldo Restante:", saldo_credito, "Créditos")
                    else:
                        print("ERRO! Créditos Insuficiente!!!")
                        print("Valor da Passagem: R$", preco_passagem)
                        print("Crédito Atual: R$", saldo_credito, "Créditos")
                #   Atualizar Senha
                elif(opcao == 4):
                    print("Cliente:", usuario_nome)
                    usuario_senha = input("Digite a Nova Senha: ")
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", usuario_senha)
                elif(opcao == 5):
                    print("ENCERRANDO SESSÃO!!!")
                #   Erro de Opção
                else:
                    print("OPÇÃO INVALIDA!!!")
    elif(opcao == 2):
        #   Login ADMINISTRADOR
        tentativa = 4
        while tentativa > 0:
            print("           LOGIN ADMINISTRADOR")
            print("=====================================")
            login_nome_admin = input("Digite o Nome de ADMINISTRADOR: ")
            login_senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
            print("=====================================")
            if(login_nome_admin == admin_nome and login_senha_admin == admin_senha):
                tentativa = 0
            else:
                print("Nome ou Senha Invalida!!!")
                tentativa = tentativa - 1
                print("Tentativas Restantes:", tentativa, "Tentativa")
                print("=====================================")
                if(tentativa == 0):
                    print("Voltando Para o Menu!!!")
        #   Menu Administrador
        if(login_nome_admin == admin_nome and login_senha_admin == admin_senha):
            while opcao != 5:
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Créditos do Usuário.")
                print("2 - Visualizar Preço da Passagem.")
                print("3 - Atualizar o Valor da Passagem.")
                print("4 - Atualizar Senha de Administrador.")
                print("5 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = int(input("Digite a Sua Opção:"))
                print("=====================================")
                #   Visualizar Créditos do Usuário
                if(opcao == 1):
                    print("Nome do Cliente:", usuario_nome)
                    print("Créditos Atuais: R$", saldo_credito)
                #   Visualizar Preço da Passagem
                elif(opcao == 2):
                    print("Preço da Passagem: R$", preco_passagem)
                #   Atualizar o Valor da Passagem
                elif(opcao == 3):
                    preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                #   Atualizar Senha de Administrador    
                elif(opcao == 4):
                    print("Administrador:", admin_nome)
                    admin_senha = input("Digite a Nova Senha: ")
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", admin_senha)
                #   Encerrando Sessão
                elif(opcao == 5):
                    print("ENCERRANDO SESSÃO!!!")
                #   Erro de Opção
                else:
                    print("OPÇÃO INVALIDA!!!")
    elif(opcao == 3):
        print("ENCERRANDO O PROGRAMA!!!")
    else:
        print("OPÇÃO INVALIDA!!!")