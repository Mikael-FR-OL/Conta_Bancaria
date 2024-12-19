from Conta import *

def criar_conta(senha, nome, saldo, limite):
    """
    Cria uma conta bancária com as informações fornecidas.
    Retorna um dicionário com os dados da conta.
    """
    conta = {"senha": senha, "nome": nome, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    """
    Deposita um valor na conta. O valor deve ser positivo.
    """
    if valor > 0:
        conta["saldo"] += valor
        print(f"Depósito de {valor} realizado com sucesso.")
    else:
        print("Valor de depósito inválido. Deve ser maior que zero.")


def retira(conta, valor):
    """
    Retira um valor da conta, respeitando o saldo disponível.
    Considera o limite da conta, permitindo retirar até o limite.
    """
    if valor > 0:
        # Verificar se há saldo suficiente (saldo + limite)
        if conta["saldo"] + conta["limite"] >= valor:
            conta["saldo"] -= valor
            print(f"Retirada de {valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente para a retirada.")
    else:
        print("Valor de retirada inválido. Deve ser maior que zero.")


def extrato(conta):
    """
    Exibe o extrato com o saldo atual da conta.
    """
    print(f"Saldo atual: {conta['saldo']}")
    print(f"Limite de crédito disponível: {conta['limite']}")
