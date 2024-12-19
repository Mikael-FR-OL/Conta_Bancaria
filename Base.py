def criar_conta(senha, nome, saldo, limite):
    conta = {"senha": senha, "nome": nome, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor
def retira(conta, valor):
    conta["saldo"] -= valor
def extrato(conta):
   print("saldo {}".format(conta["saldo"]))
