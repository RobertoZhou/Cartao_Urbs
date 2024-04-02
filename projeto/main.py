print("=====================================")
print("                 MENU")
print("=====================================")
print("1 - Cliente.")
print("2 - Administrador.")
print("=====================================")
print("Por Favor, Escolha entre 1 ou 2")
opcao = input("Qual Usuário acima você é: ")
print("=====================================")


preco_passagem = 6
saldo_usuario = 0
encerrar_sessao = 0
senha_acesso = "4321"

#   Menu Administrador
if(opcao == "2"):
    senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
    if(senha_admin == senha_acesso):
        print("=====================================")
        print("         MENU ADMINISTRADOR")
        print("=====================================")
        print("1 - Visualizar Créditos do Usuário.")
        print("2 - Visualizar Preço da Passagem.")
        print("3 - Atualizar o Valor da Passagem.")
        print("4 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")
    #   Erro de senha invalida
    if(senha_admin != senha_acesso):
        print("SENHA INCORRETA!!!")
        print("Ultima Tentativa! Proximo Erro Encerrando o Programa!!!")
        opcao = 0
        print("=====================================")
        senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
        if(senha_admin == senha_acesso):
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Créditos do Usuário.")
            print("2 - Visualizar Preço da Passagem.")
            print("3 - Atualizar o Valor da Passagem.")
            print("4 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
    #   Erro de senha invalida
    if(senha_admin != senha_acesso):
        print("SENHA INCORRETA!!!")
        print("ENCERRANDO O PROGRAMA!!!") 
#   Visualizar Créditos do Usuário
    if(opcao == "1"):
        print("O Usuário Possui: R$", saldo_usuario, "Créditos")
        print("=====================================")
        print("         MENU ADMINISTRADOR")
        print("=====================================")
        print("1 - Visualizar Preço da Passagem.")
        print("2 - Atualizar o Valor da Passagem.")
        print("3 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")
        #   Encerrar Sessão
        if(opcao == "3"):
            encerrar_sessao = 1
            opcao = "0"
#   Visualizar Preço da Passagem
        if(opcao == "1"):
            print("Preço da Passagem: R$", preco_passagem)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Atualizar o Valor da Passagem.")
            print("2 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
#   Atualizar o Valor da Passagem
            if(opcao == "1"):
                print("Preço da Passagem Atual: R$", preco_passagem)
                preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                print("Novo Preço da Passagem: R$", preco_passagem)
                encerrar_sessao = 1
                opcao = "0"
#   Visualizar Créditos do Usuário
        if(opcao == "2"):
            print("Preço da Passagem Atual: R$", preco_passagem)
            preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
            print("Novo Preço da Passagem: R$", preco_passagem)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Créditos do Usuário.")
            print("2 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
            if(opcao == "1"):
                print("O Cliente Possui:", saldo_usuario)
                encerrar_sessao = 1
                opcao = "0"

    #   Visualizar Preço da Passagem
    if(opcao == "2"):
        print("Preço da Passagem: R$", preco_passagem)
        print("=====================================")
        print("         MENU ADMINISTRADOR")
        print("=====================================")
        print("1 - Visualizar Preço da Passagem.")
        print("2 - Atualizar o Valor da Passagem.")
        print("3 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")

        #   Encerrar Sessão
        if(opcao == "3"):
            encerrar_sessao = 1
            opcao = "0"

    #   Visualizar Créditos do Usuário
        if(opcao == "1"):
            print("O Cliente Possui:", saldo_usuario)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Atualizar o Valor da Passagem.")
            print("2 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")

    #   Atualizar o Valor da Passagem
            if(opcao == "1"):
                print("Preço da Passagem Atual: R$", preco_passagem)
                preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                print("Novo Preço da Passagem: R$", preco_passagem)
                encerrar_sessao = 1
                opcao = "0"
        if(opcao == "2"):
            print("Preço da Passagem Atual: R$", preco_passagem)
            preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
            print("Novo Preço da Passagem: R$", preco_passagem)
            print("Preço da Passagem: R$", preco_passagem)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Preço da Passagem.")
            print("2 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")

        #   Visualizar Créditos do Usuário
            if(opcao == "1"):
                print("O Cliente Possui:", saldo_usuario)
                encerrar_sessao = 1
                opcao = "0"

    #   Atualizar o Valor da Passagem
if(opcao == "3"):
    print("Preço da Passagem Atual: R$", preco_passagem)
    preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
    print("Novo Preço da Passagem: R$", preco_passagem)
    print("=====================================")
    print("         MENU ADMINISTRADOR")
    print("=====================================")
    print("1 - Visualizar Créditos do Usuário.")
    print("2 - Visualizar Preço da Passagem.")
    print("3 - ENCERRANDO SESSÃO.")
    print("=====================================")
    opcao = input("Digite a Sua Opção:")
    print("=====================================")
    #   Encerrando Sessão
    if(opcao == "3"):
        encerrar_sessao = 1
        opcao = "0"
#   Visualizar Créditos do Usuário
    if(opcao == "1"):
        print("O Usuário Possui: R$", saldo_usuario, "Créditos")
        print("=====================================")
        print("         MENU ADMINISTRADOR")
        print("=====================================")
        print("1 - Visualizar Preço da Passagem.")
        print("2 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")
        #   Visualizar Preço da Passagem
        if(opcao == "1"):
            print("Preço da Passagem Atual: R$", preco_passagem)
            encerrar_sessao = 1
            opcao = "0"
#   Visualizar Preço da Passagem
    if(opcao == "2"):
        print("O Usuário Possui: R$", saldo_usuario)
        print("=====================================")
        print("         MENU ADMINISTRADOR")
        print("=====================================")
        print("1 - Visualizar Créditos do Usuário.")
        print("3 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")
        #   Visualizar Créditos do Usuário
        if(opcao == "1"):
            print("O Usuário Possui: R$", saldo_usuario, "Créditos")
            encerrar_sessao = 1
            opcao = "0"
            
#   Encerrar Sessão
if(opcao == "2"):
    encerrar_sessao = 1
    opcao = "0"


if(encerrar_sessao == 1):
    print("=====================================")
    print("ENCERRANDO SESSÃO")
    print("Entrando no Modo Cliente")
#   Menu Cliente
if(opcao == "1" or encerrar_sessao == 1):
    print("=====================================")
    print("             MENU CLIENTE")
    print("=====================================")
    print("1 - Depositar Crédito")
    print("2 - Utilizar o Cartão.")
    print("3 - ENCERRANDO SESSÃO.")
    print("=====================================")
    opcao = input("Digite a Sua Opção:")
    print("=====================================")
#   Depositar Crédito
    if(opcao == "1"):
        print("Valor da Passagem: R$", preco_passagem)
        valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
        saldo_usuario = valor_depositado + saldo_usuario
        print("Saldo Atual: R$", saldo_usuario, "Créditos")

        print("=====================================")
        print("             MENU CLIENTE")
        print("=====================================")
        print("1 - Utilizar o Cartão.")
        print("2 - ENCERRANDO SESSÃO.")
        print("=====================================")
        opcao = input("Digite a Sua Opção:")
        print("=====================================")

        if(opcao == "1"):
            if(saldo_usuario > preco_passagem):
                saldo_usuario = saldo_usuario - preco_passagem
                print("Cartão Passado Com Sucesso!")
                print("Boa Viagem!!!")
                print("Saldo Restante:", saldo_usuario, "Créditos")
            if(saldo_usuario <= preco_passagem):
                print("ERRO! Crédito Insuficiente")
                print("Crédito Atual:", saldo_usuario, "Créditos")
                print("Valor da Passagem: R$", preco_passagem)
                print("=====================================")
                print("Por favor, Digite S ou N!!!")
                verificar_escolha = input("Depositar Créditos na sua Conta [S / N]: ")
                if(verificar_escolha == "S" or verificar_escolha == "s"):
                    valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                    saldo_usuario = valor_depositado + saldo_usuario
                    print("Saldo Atual: R$", saldo_usuario, "Créditos")

                    print("=====================================")
                    print("             MENU CLIENTE")
                    print("=====================================")
                    print("1 - Utilizar o Cartão.")
                    print("2 - ENCERRANDO SESSÃO.")
                    print("=====================================")
                    opcao = input("Digite a Sua Opção:")
                    print("=====================================")

                    if(opcao == "1"):
                        if(saldo_usuario > preco_passagem):
                            saldo_usuario = saldo_usuario - preco_passagem
                            print("Cartão Passado Com Sucesso!")
                            print("Boa Viagem!!!")
                            print("Saldo Restante:", saldo_usuario, "Créditos")
                        if(saldo_usuario <= preco_passagem):
                            print("ERRO! Crédito Insuficiente")
                            print("Crédito Atual:", saldo_usuario, "Créditos")
    
    if(opcao == "2"):
        if(saldo_usuario > preco_passagem):
            saldo_usuario = saldo_usuario - preco_passagem
            print("Cartão Passado Com Sucesso!")
            print("Boa Viagem!!!")
            print("Saldo Restante:", saldo_usuario, "Créditos")
        if(saldo_usuario <= preco_passagem):
            print("ERRO! Crédito Insuficiente")
            print("Crédito Atual:", saldo_usuario, "Créditos")
            print("Valor da Passagem: R$", preco_passagem)
            print("=====================================")
            print("Por favor, Digite S ou N!!!")
            verificar_escolha = input("Depositar Créditos na sua Conta [S / N]: ")
            if(verificar_escolha == "S" or verificar_escolha == "s"):
                valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                saldo_usuario = valor_depositado + saldo_usuario
                print("Saldo Atual: R$", saldo_usuario, "Créditos")

                print("=====================================")
                print("             MENU CLIENTE")
                print("=====================================")
                print("1 - Utilizar o Cartão.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")

                if(opcao == "1"):
                    if(saldo_usuario > preco_passagem):
                        saldo_usuario = saldo_usuario - preco_passagem
                        print("Cartão Passado Com Sucesso!")
                        print("Boa Viagem!!!")
                        print("Saldo Restante:", saldo_usuario, "Créditos")
                    if(saldo_usuario <= preco_passagem):
                        print("ERRO! Crédito Insuficiente")
                        print("Crédito Atual:", saldo_usuario, "Créditos")
    if(opcao != "1" and opcao != "2" and opcao != "3"):
        print("Opção Invalida. Tente Novamente!!!")
    #   Encerrar Sessão
    print("ENCERRANDO SESSÃO")
    print("Por Favor, Digite S ou N!!!")
    verificar_escolha = input("Gostaria de Mudar Para modo ADMINISTRADOR [S/N]: ")
    if(verificar_escolha == "s" or verificar_escolha == "S"):
#   Menu Administrador
        senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
        if(senha_admin == senha_acesso):
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Créditos do Usuário.")
            print("2 - Visualizar Preço da Passagem.")
            print("3 - Atualizar o Valor da Passagem.")
            print("4 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
        #   Erro de senha invalida
        if(senha_admin != senha_acesso):
            print("SENHA INCORRETA!!!")
            print("Ultima Tentativa! Proximo Erro Encerrando o Programa!!!")
            opcao = 0
            print("=====================================")
            senha_admin = input("Digite a Senha de ADMINISTRADOR: ")
            if(senha_admin == senha_acesso):
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Créditos do Usuário.")
                print("2 - Visualizar Preço da Passagem.")
                print("3 - Atualizar o Valor da Passagem.")
                print("4 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
        #   Erro de senha invalida
        if(senha_admin != senha_acesso):
            print("SENHA INCORRETA!!!")
            print("ENCERRANDO O PROGRAMA!!!") 
    #   Visualizar Créditos do Usuário
        if(opcao == "1"):
            print("O Usuário Possui: R$", saldo_usuario, "Créditos")
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Preço da Passagem.")
            print("2 - Atualizar o Valor da Passagem.")
            print("3 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
            #   Encerrar Sessão
            if(opcao == "3"):
                encerrar_sessao = 1
                opcao = "0"
    #   Visualizar Preço da Passagem
            if(opcao == "1"):
                print("Preço da Passagem: R$", preco_passagem)
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Atualizar o Valor da Passagem.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
    #   Atualizar o Valor da Passagem
                if(opcao == "1"):
                    print("Preço da Passagem Atual: R$", preco_passagem)
                    preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                    print("Novo Preço da Passagem: R$", preco_passagem)
                    encerrar_sessao = 1
                    opcao = "0"
    #   Visualizar Créditos do Usuário
            if(opcao == "2"):
                print("Preço da Passagem Atual: R$", preco_passagem)
                preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                print("Novo Preço da Passagem: R$", preco_passagem)
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Créditos do Usuário.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
                if(opcao == "1"):
                    print("O Cliente Possui:", saldo_usuario)
                    encerrar_sessao = 1
                    opcao = "0"

        #   Visualizar Preço da Passagem
        if(opcao == "2"):
            print("Preço da Passagem: R$", preco_passagem)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Preço da Passagem.")
            print("2 - Atualizar o Valor da Passagem.")
            print("3 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")

            #   Encerrar Sessão
            if(opcao == "3"):
                encerrar_sessao = 1
                opcao = "0"

        #   Visualizar Créditos do Usuário
            if(opcao == "1"):
                print("O Cliente Possui:", saldo_usuario)
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Atualizar o Valor da Passagem.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")

        #   Atualizar o Valor da Passagem
                if(opcao == "1"):
                    print("Preço da Passagem Atual: R$", preco_passagem)
                    preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                    print("Novo Preço da Passagem: R$", preco_passagem)
                    encerrar_sessao = 1
                    opcao = "0"
            if(opcao == "2"):
                print("Preço da Passagem Atual: R$", preco_passagem)
                preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
                print("Novo Preço da Passagem: R$", preco_passagem)
                print("Preço da Passagem: R$", preco_passagem)
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Preço da Passagem.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")

            #   Visualizar Créditos do Usuário
                if(opcao == "1"):
                    print("O Cliente Possui:", saldo_usuario)
                    encerrar_sessao = 1
                    opcao = "0"

        #   Atualizar o Valor da Passagem
        if(opcao == "3"):
            print("Preço da Passagem Atual: R$", preco_passagem)
            preco_passagem = float(input("Digite o Novo Preço da Passagem: R$"))
            print("Novo Preço da Passagem: R$", preco_passagem)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Créditos do Usuário.")
            print("2 - Visualizar Preço da Passagem.")
            print("3 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
            #   Encerrando Sessão
            if(opcao == "3"):
                encerrar_sessao = 1
                opcao = "0"
        #   Visualizar Créditos do Usuário
            if(opcao == "1"):
                print("O Usuário Possui: R$", saldo_usuario, "Créditos")
                print("=====================================")
                print("         MENU ADMINISTRADOR")
                print("=====================================")
                print("1 - Visualizar Preço da Passagem.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")
                #   Visualizar Preço da Passagem
                if(opcao == "1"):
                    print("Preço da Passagem Atual: R$", preco_passagem)
                    encerrar_sessao = 1
                    opcao = "0"
    #   Visualizar Preço da Passagem
        if(opcao == "2"):
            print("O Usuário Possui: R$", saldo_usuario)
            print("=====================================")
            print("         MENU ADMINISTRADOR")
            print("=====================================")
            print("1 - Visualizar Créditos do Usuário.")
            print("3 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
            #   Visualizar Créditos do Usuário
            if(opcao == "1"):
                print("O Usuário Possui: R$", saldo_usuario, "Créditos")
                encerrar_sessao = 1
                opcao = "0"
                
    #   Encerrar Sessão
        if(opcao == "2"):
            encerrar_sessao = 1
            opcao = "0"


        if(encerrar_sessao == 1):
            print("=====================================")
            print("ENCERRANDO SESSÃO")
            print("Entrando no Modo Cliente")
        #   Menu Cliente
        if(opcao == "1" or encerrar_sessao == 1):
            print("=====================================")
            print("             MENU CLIENTE")
            print("=====================================")
            print("1 - Depositar Crédito")
            print("2 - Utilizar o Cartão.")
            print("3 - ENCERRANDO SESSÃO.")
            print("=====================================")
            opcao = input("Digite a Sua Opção:")
            print("=====================================")
        #   Depositar Crédito
            if(opcao == "1"):
                print("Valor da Passagem: R$", preco_passagem)
                valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                saldo_usuario = valor_depositado + saldo_usuario
                print("Saldo Atual: R$", saldo_usuario, "Créditos")

                print("=====================================")
                print("             MENU CLIENTE")
                print("=====================================")
                print("1 - Utilizar o Cartão.")
                print("2 - ENCERRANDO SESSÃO.")
                print("=====================================")
                opcao = input("Digite a Sua Opção:")
                print("=====================================")

                if(opcao == "1"):
                    if(saldo_usuario > preco_passagem):
                        saldo_usuario = saldo_usuario - preco_passagem
                        print("Cartão Passado Com Sucesso!")
                        print("Boa Viagem!!!")
                        print("Saldo Restante:", saldo_usuario, "Créditos")
                    if(saldo_usuario <= preco_passagem):
                        print("ERRO! Crédito Insuficiente")
                        print("Crédito Atual:", saldo_usuario, "Créditos")
                        print("Valor da Passagem: R$", preco_passagem)
                        print("=====================================")
                        print("Por favor, Digite S ou N!!!")
                        verificar_escolha = input("Depositar Créditos na sua Conta [S / N]: ")
                        if(verificar_escolha == "S" or verificar_escolha == "s"):
                            valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                            saldo_usuario = valor_depositado + saldo_usuario
                            print("Saldo Atual: R$", saldo_usuario, "Créditos")

                            print("=====================================")
                            print("             MENU CLIENTE")
                            print("=====================================")
                            print("1 - Utilizar o Cartão.")
                            print("2 - ENCERRANDO SESSÃO.")
                            print("=====================================")
                            opcao = input("Digite a Sua Opção:")
                            print("=====================================")

                            if(opcao == "1"):
                                if(saldo_usuario > preco_passagem):
                                    saldo_usuario = saldo_usuario - preco_passagem
                                    print("Cartão Passado Com Sucesso!")
                                    print("Boa Viagem!!!")
                                    print("Saldo Restante:", saldo_usuario, "Créditos")
                                if(saldo_usuario <= preco_passagem):
                                    print("ERRO! Crédito Insuficiente")
                                    print("Crédito Atual:", saldo_usuario, "Créditos")
            
            if(opcao == "2"):
                if(saldo_usuario > preco_passagem):
                    saldo_usuario = saldo_usuario - preco_passagem
                    print("Cartão Passado Com Sucesso!")
                    print("Boa Viagem!!!")
                    print("Saldo Restante:", saldo_usuario, "Créditos")
                if(saldo_usuario <= preco_passagem):
                    print("ERRO! Crédito Insuficiente")
                    print("Crédito Atual:", saldo_usuario, "Créditos")
                    print("Valor da Passagem: R$", preco_passagem)
                    print("=====================================")
                    print("Por favor, Digite S ou N!!!")
                    verificar_escolha = input("Depositar Créditos na sua Conta [S / N]: ")
                    if(verificar_escolha == "S" or verificar_escolha == "s"):
                        valor_depositado = float(input("Digite o Valor Que Gostaria de Depositar: R$"))
                        saldo_usuario = valor_depositado + saldo_usuario
                        print("Saldo Atual: R$", saldo_usuario, "Créditos")

                        print("=====================================")
                        print("             MENU CLIENTE")
                        print("=====================================")
                        print("1 - Utilizar o Cartão.")
                        print("2 - ENCERRANDO SESSÃO.")
                        print("=====================================")
                        opcao = input("Digite a Sua Opção:")
                        print("=====================================")

                        if(opcao == "1"):
                            if(saldo_usuario > preco_passagem):
                                saldo_usuario = saldo_usuario - preco_passagem
                                print("Cartão Passado Com Sucesso!")
                                print("Boa Viagem!!!")
                                print("Saldo Restante:", saldo_usuario, "Créditos")
                            if(saldo_usuario <= preco_passagem):
                                print("ERRO! Crédito Insuficiente")
                                print("Crédito Atual:", saldo_usuario, "Créditos")
            if(opcao != "1" and opcao != "2" and opcao != "3"):
                print("Opção Invalida. Tente Novamente!!!")