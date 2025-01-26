# Solicita ao usuário o valor do depósito e o armazena na variável 'valor'
valor = float(input())

# Inicializa o saldo da conta como zero
saldo = 0

# Verifica se o 'valor' digitado pelo usuário é maior do que zero
if valor > 0:
    saldo += valor
    print("Depósito realizado com sucesso!")
    print(f'Saldo atual: R$ {saldo:.2f}')
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor inválido! Digite um valor maior que zero.")
