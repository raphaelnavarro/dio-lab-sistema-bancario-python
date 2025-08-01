def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("⚠️ Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("⚠️ Limite de saques diários atingido.")
    elif valor > limite:
        print("⚠️ Valor do saque excede o limite por operação.")
    elif valor > saldo:
        print("⚠️ Saldo insuficiente.")
    elif valor <= 0:
        print("⚠️ Valor inválido para saque.")
    else:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n📄 EXTRATO:")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo: R${saldo:.2f}\n")


def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print("⚠️ Usuário já cadastrado.")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("✅ Usuário cadastrado com sucesso!")


def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do titular da conta: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("⚠️ Usuário não encontrado. Cadastre o usuário primeiro.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print("✅ Conta criada com sucesso!")
    return conta


# =============================== #
# 👇 PROGRAMA PRINCIPAL AQUI 👇   #
# =============================== #

AGENCIA_PADRAO = "0001"
usuarios = []
contas = []

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("""
=========== MENU ===========
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
============================
""")
    opcao = input("Escolha uma opção: ").lower().strip()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "nu":
        cadastrar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = cadastrar_conta(AGENCIA_PADRAO, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "lc":
        for conta in contas:
            print(f"\nAgência: {conta['agencia']}")
            print(f"Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']}")
        if not contas:
            print("Nenhuma conta cadastrada.")

    elif opcao == "q":
        print("✅ Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("⚠️ Operação inválida. Tente novamente.")

