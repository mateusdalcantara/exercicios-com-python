valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def investimento(valor_inicial, taxa_juros, periodo):
    resultado = valor_inicial * (1 + taxa_juros)**periodo
    return resultado

# Inicialize o valor final com o valor inicial
valor_final = valor_inicial

# Itere com base no periodo em anos
for ano in range(periodo):
    valor_final = investimento(valor_final, taxa_juros, 1)

print(f'Valor final do investimento: R$ {valor_final:.2f}')
