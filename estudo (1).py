#1- saldo // 2-depositar // 3-tirar dinheiro
running=True
tela_inicio= ("1-Saldo", "2-Depositar", "3-Sacar dinheiro", "4-Sair")
saldo=0



while running:
    print("///////////////Banco UP!///////////////")
    for menu in tela_inicio:
        print(menu)
    print()
    operação=int(input("Digite o número da sua operação: "))
    if 1 > operação or operação> 4 or operação is str:
        print("Operação invalida, tente novamente")
    elif operação==1:
        print(f"O seu Saldo é de: {saldo}R$")
        continua=input("Deseja fazer mais operações? (S/N): ").upper()
        if continua=="S":
            continue
        else:
            print("Finalizando...")
            running=False

    elif operação==2:
        deposito=float(input("Digite o valor que deseja depositar em sua conta (utilize .): "))
        saldo+=deposito
        print("Saldo atualizado!")
        continua = input("Deseja fazer mais operações? (S/N): ").upper()
        if continua == "S":
            continue
        else:
            print("Finalizando...")
            running = False

    elif operação==3:
        saque=(float(input(f"Digite o valor para sacar (saldo disponivel {saldo})")))
        while saque>saldo:
            print("Saldo insuficientem, tente novamente")
        else:
            saldo-=saque
            print("Resgate Efetuado!")
        continua = input("Deseja fazer mais operações? (S/N): ").upper()
        if continua == "S":
            continue
        else:
            print("Finalizando...")
            running = False

    elif operação==4:
        print("Saindo do programa, volte sempre!")
        break
