verificar_registro = 0
while True:
    if(verificar_registro == 0):
        print("=====================================")
        print("         REGISTRAR CLIENTE")
        print("=====================================")
        usuario_nome = input("Digite Seu Nome de Usúario: ")
        if(usuario_nome.strip() != ""):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo com seu Nome!!!")
    if(verificar_registro == 1):
        usuario_senha = input("Digite Sua Senha: ")
        if(usuario_senha.strip() != ""):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo Com Sua Senha!!!")

    if(verificar_registro == 2):
        print("=====================================")
        print("      REGISTRAR ADMINISTRADOR")
        print("=====================================")
        admin_nome = input("Digite Seu Nome: ")
        if(admin_nome.strip() != ""):
            verificar_registro = verificar_registro + 1
        else:
            print("Por Favor, Preencha o Campo com seu Nome!!!")
    if(verificar_registro == 3):
        admin_senha = input("Digite Sua Senha: ")
        if(admin_senha.strip() != ""):
            verificar_registro = verificar_registro + 1
            preco_passagem = float(input("Por Favor, Digite o Valor da Passagem: R$"))
            break
        else:
            print("Por Favor, Preencha o Campo Com Sua Senha!!!")

saldo_credito = 0
encerrar_programa = True
while encerrar_programa:
    print("=====================================")
    print("                 MENU")
    print("=====================================")
    print("1 - Cliente.")
    print("2 - Administrador.")
    print("3 - Encerrar Sessão.")
    print("=====================================")
    print("Por Favor, Escolha entre [ 1, 2 e 3 ]")
    opcao = input("Qual Usuário acima você é: ")
    print("=====================================")

    if(opcao == "1"):
        #   Login Cliente
        contador = 4
        while contador != 0:
            print("            LOGIN CLIENTE")
            print("=====================================")
            login_nome_usuario = input("Digite o Nome de Usuário: ")
            login_senha_usuario = input("Digite a Senha de Usuário: ")
            print("=====================================")
            if(login_nome_usuario == usuario_nome and login_senha_usuario == usuario_senha):
                contador = 0
            else:
                print("Nome ou Senha Invalida!!!")
                contador = contador - 1
                if(contador == 0):
                    encerrar_login = False
                else:
                    print("Chance de Tentativa:", contador, "Tentativa")
        #   Menu Cliente
        if(login_nome_usuario == usuario_nome and login_senha_usuario == usuario_senha):
            parada_login = True
            while parada_login:
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
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
                #   Visualizar Créditos
                if(opcao == "1"):
                    print("O Cliente:", usuario_nome)
                    print("Créditos Possuído: R$", saldo_credito)

                #   Depositar Crédito
                elif(opcao == "2"):
                    parada = True
                    while parada:
                        print("=====================================")
                        print("O Cliente:", usuario_nome)
                        print("Créditos Possuído: R$", saldo_credito)
                        print("Valor da Passagem: R$", preco_passagem)
                        print("=====================================")
                        deposito_credito = input("Digite o Valor Que Gostaria de Depositar: R$").strip()
                        print("=====================================")
                        #   Verificar se e um numero
                        if("1" in deposito_credito or "2" in deposito_credito or "3" in deposito_credito or "4" in deposito_credito or "5" in deposito_credito or "6" in deposito_credito or "7" in deposito_credito or "8" in deposito_credito or "9" in deposito_credito or "0" in deposito_credito):
                            saldo_credito = saldo_credito + float(deposito_credito)
                            print("Saldo Atual: R$", saldo_credito)
                            parada = False
                        else:
                            print("Valor Informado Invalido!!!")
                #   Utilizar o Cartão
                elif(opcao == "3"):
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
                elif(opcao == "4"):
                    print("Cliente:", usuario_nome)
                    usuario_senha = input("Digite a Nova Senha: ")
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", usuario_senha)
                elif(opcao == "5"):
                    print("ENCERRANDO SESSÃO!!!")
                    parada_login = False
                else:
                    print("OPÇÃO INVALIDA!!!")
    if(opcao == "2"):
        #   Login ADMINISTRADOR
        contador = 4
        while contador != 0:
            print("           LOGIN ADMINISTRADOR")
            print("=====================================")
            login_nome_admin = input("Digite o Nome de ADMINISTRADOR: ")
            login_senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
            print("=====================================")
            if(login_nome_admin == admin_nome and login_senha_admin == admin_senha):
                contador = 0
            else:
                print("Nome ou Senha Invalida!!!")
                contador = contador - 1
                if(contador == 0):
                    encerrar_login = False
                else:
                    print("Chance de Tentativa:", contador, "Tentativa")
        #   Menu Administrador
        if(login_nome_admin == admin_nome and login_senha_admin == admin_senha):
            parada_login = True
            while parada_login:
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Créditos do Usuário.")
                print("2 - Visualizar Preço da Passagem.")
                print("3 - Atualizar o Valor da Passagem.")
                print("4 - Atualizar Senha de Administrador.")
                print("5 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
                #   Visualizar Créditos do Usuário
                if(opcao == "1"):
                    print("Nome do Cliente:", usuario_nome)
                    print("Créditos Atuais: R$", saldo_credito)
                #   Visualizar Preço da Passagem
                elif(opcao == "2"):
                    print("Preço da Passagem: R$", preco_passagem)
                #   Atualizar o Valor da Passagem
                elif(opcao == "3"):
                    novo_preço = input("Digite o Novo Preço da Passagem: R$")
                    #   Verificar se e um numero
                    if("1" in novo_preço or "2" in novo_preço or "3" in novo_preço or "4" in novo_preço or "5" in novo_preço or "6" in novo_preço or "7" in novo_preço or "8" in novo_preço or "9" in novo_preço or "0" in novo_preço):
                        preco_passagem = novo_preço
                    else:
                        print("Valor Informado Invalido!!!")
                #   Atualizar Senha de Administrador    
                elif(opcao == "4"):
                    print("Administrador:", admin_nome)
                    admin_senha = input("Digite a Nova Senha: ")
                    print("Nova Senha Cadastrado Com Sucesso")
                    print("Nova Senha:", admin_senha)
                #   Encerrar Sessão
                elif(opcao == "5"):
                    print("ENCERRANDO SESSÃO!!!")
                    parada_login = False
    elif(opcao == "3"):
        print("ENCERRANDO O PROGRAMA!!!")
        encerrar_programa = False
    else:
        print("OPÇÃO INVALIDA!!!")