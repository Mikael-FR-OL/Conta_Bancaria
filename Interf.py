from Base import *
senha = int(input("Entre com uma senha: "))
nome = str(input("Entre com o nome: "))
saldo = int(input("Entre com o saldo: "))
limite = int(input("Informe o seu limite atual: "))

conta = criar_conta(senha, nome, saldo, limite)
print(conta)

deposita(conta, 200)
retira(conta, 100)
extrato(conta)