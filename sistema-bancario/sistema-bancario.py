saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

itemMenu = """

[d] deposito
[s] saque
[e] extrato
[q] sair

"""

while True:
    valor_menu = input(itemMenu)
    if valor_menu == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: .2f}\n"
        else: 
            print("Operação falhou: o valor informado é inválido.")

    elif valor_menu == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("peraçã falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque: .2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif valor_menu == "e":
        print("EXTRATO".center(15, "*"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("".center(22, "*"))

    elif valor_menu == "q":
        break

    else:
        print("Operação inválida, por favor selecioa novamente a operação desejada.")
