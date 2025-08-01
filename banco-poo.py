class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
    
    def __str__(self):
        return f"Cliente: {self.nome} - CPF: {self.cpf}"


class ContaBancaria:
    def __init__(self, agencia, numero_conta, cliente, limite=500.0, limite_saques=3):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.cliente = cliente  # Referência para o objeto Cliente
        self.saldo = 0.0
        self.extrato = ""
        self.limite = limite
        self.numero_saques = 0
        self.limite_saques = limite_saques
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("Limite diário de saques atingido.")
        elif valor > self.limite:
            print(f"Valor do saque excede o limite por operação de R${self.limite:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            self.saldo -= valor
            self.extrato += f"Saque: R${valor:.2f}\n"
            self.numero_saques += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
    
    def exibir_extrato(self):
        print("\n=== EXTRATO ===")
        print(self.extrato if self.extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("================\n")
    
    def __str__(self):
        return f"Conta {self.numero_conta} - Agência {self.agencia} - Titular: {self.cliente.nome}"


# Funções auxiliares para cadastro e menu
def cadastrar_cliente(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    # Verifica se cliente já existe
    if any(cliente.cpf == cpf for cliente in usuarios):
        print("Cliente já cadastrado.")
        return None
    
    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ").strip()
    
    cliente = Cliente(nome, cpf, data_nascimento, endereco)
    usuarios.append(cliente)
    print("Cliente cadastrado com sucesso!")
    return cliente

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do titular da conta: ").strip()
    cliente = next((c for c in usuarios if c.cpf == cpf), None)
    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        return None
    conta = ContaBancaria(agencia, numero_conta, cliente)
    print("Conta criada com sucesso!")
    return conta


# Programa principal
def main():
    AGENCIA_PADRAO = "0001"
    usuarios = []
    contas = []

    while True:
        print("""
========== MENU ==========
[1] Cadastrar cliente
[2] Cadastrar conta
[3] Depositar
[4] Sacar
[5] Extrato
[6] Listar contas
[0] Sair
==========================
""")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(usuarios)

        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA_PADRAO, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "3":
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue
            numero = int(input("Informe o número da conta para depósito: "))
            conta = next((c for c in contas if c.numero_conta == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            valor = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)

        elif opcao == "4":
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue
            numero = int(input("Informe o número da conta para saque: "))
            conta = next((c for c in contas if c.numero_conta == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            valor = float(input("Informe o valor do saque: "))
            conta.sacar(valor)

        elif opcao == "5":
            if not contas:
                print("Nenhuma conta cadastrada.")
                continue
            numero = int(input("Informe o número da conta para extrato: "))
            conta = next((c for c in contas if c.numero_conta == numero), None)
            if not conta:
                print("Conta não encontrada.")
                continue
            conta.exibir_extrato()

        elif opcao == "6":
            if not contas:
                print("Nenhuma conta cadastrada.")
            else:
                print("\n=== Contas cadastradas ===")
                for conta in contas:
                    print(conta)
                print("==========================\n")

        elif opcao == "0":
            print("Encerrando sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
