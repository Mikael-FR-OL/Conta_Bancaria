from Base import Conta


senha = int(input("Entre com uma senha: "))
nome = str(input("Entre com o nome: "))
saldo = int(input("Entre com o saldo: "))
limite = int(input("Informe o seu limite atual: "))


conta = Conta(numero=123, titular=nome, saldo=saldo, limite=limite)
print(f"Conta criada para {conta.titular}: {conta.saldo} de saldo e {conta.limite} de limite")


conta.deposita(200)
print("Após depósito de 200:")
conta.extrato()

conta.saca(100)
print("Após saque de 100:")
conta.extrato()

