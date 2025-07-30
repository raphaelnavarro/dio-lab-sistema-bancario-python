menu = """
=== MENU ===

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

Escolha uma opção: """

saldo_atual = 0
limite_diario = 500
historico = ""
saques_realizados = 0
MAX_SAQUES = 3

while True:
    escolha = input(menu)

    if escolha == "1":
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito > 0:
            saldo_atual += deposito
            historico += f"Depósito realizado: R$ {deposito:.2f}\n"
        else:
            print("Erro: valor inválido para depósito.")

    elif escolha == "2":
        saque = float(input("Digite o valor do saque: "))

        sem_saldo = saque > saldo_atual
        acima_limite = saque > limite_diario
        limite_saques = saques_realizados >= MAX_SAQUES

        if sem_saldo:
            print("Erro: saldo insuficiente.")
        elif acima_limite:
            print("Erro: valor acima do limite por operação.")
        elif limite_saques:
            print("Erro: número de saques diários excedido.")
        elif saque > 0:
            saldo_atual -= saque
            historico += f"Saque efetuado: R$ {saque:.2f}\n"
            saques_realizados += 1
        else:
            print("Erro: valor inválido para saque.")

    elif escolha == "3":
        print("\n======= EXTRATO =======")
        print("Nenhuma transação registrada." if not historico else historico)
        print(f"Saldo atual: R$ {saldo_atual:.2f}")
        print("========================")

    elif escolha == "0":
        print("Encerrando sessão. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")


