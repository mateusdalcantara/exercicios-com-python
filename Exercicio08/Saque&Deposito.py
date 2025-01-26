# Entrada de dados.
saldoTotal = int(input())
valorSaque = int(input())

# Função para realizar o saque e retornar o novo saldo.
def saque(saldo, saque):
    novoSaldo = saldo - saque
    return novoSaldo

# Verificar se o saldo é suficiente para o saque.
if saldoTotal >= valorSaque:
    novoSaldo = saque(saldoTotal, valorSaque)
    print(f"Saque realizado com sucesso. Novo saldo: {novoSaldo}")
else:
    print("Saldo insuficiente. Saque nao realizado!")
