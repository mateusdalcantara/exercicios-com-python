def calcular_saldo(saldo):
    valor_salario + valor_beneficio - valor_retirada
    return saldo

valor_salario = float(input())
valor_beneficio = float(input())
valor_retirada = float(input())

valor_imposto = calcular_saldo(valor_salario)
saida = valor_salario - valor_retirada + valor_beneficio
print(f'Saldo atualizado na conta: {saida:.1f}')
    