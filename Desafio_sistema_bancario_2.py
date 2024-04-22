def func_menu():
    return input("""
___________________________________
Selecione o Serviço desejado:

SERVIÇO         -       TECLA

Saque           -       1
Deposito        -       2
Extrato         -       3
Novo Usuário    -       4
Nova Conta      -       5
Sair            -       0
___________________________________
""")
    
def func_deposito():
    global saldo, extrato
    try:
        valor = float(input("Digite o Valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposíto efetuado com sucesso! \n")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Erro, favor digitar um valor númerico")
    return 

def func_saque():
    global saldo, extrato, limite, LIMITE_SAQUES, numero_saques
    try:
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso! \n")

        else:
            print("Operação falhou! O valor informado é inválido.")
        return
    except ValueError:

        print("Erro, favor digitar um valor númerico")
        return 0
    
def func_imprime_extrato():
    global extrato;
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def func_criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = func_filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def func_filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def func_criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:

    opcao = func_menu()

    if opcao == "1":
        func_saque()

    elif opcao == "2":
        func_deposito()

    elif opcao == "3":
        func_imprime_extrato()
    
    elif opcao == "4":
        func_criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = func_criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
