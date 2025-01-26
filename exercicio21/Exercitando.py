"""
DONE - Faça um programa que leia um número inteiro e imprima-o.
DONE - Faça um programa que peça para o usuário digitar três valores inteiros e imprima a soma deles.
DONE - Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

"""


def leia_um_numero(a):
    return a


def tres_valores_inteiros(a, b, c):
    return a + b + c


def receba_tres_valores(a, b, c):
    soma_dos_quadrados = a ** 2 + b ** 2 + c ** 2
    return soma_dos_quadrados


a = int(input("Informe o valor inteiro de A: "))
b = int(input("Informe o valor inteiro de B: "))
c = int(input("Informe o valor inteiro de C: "))

print(f"Leia e imprima um valor inteiro: {leia_um_numero(a)}")
print(f"Leia três valores inteiros e imprima a soma deles: {tres_valores_inteiros(a, b, c)}")
print(f"Leia três valores e apresente a soma dos quadrados dos valores lidos: {receba_tres_valores(a, b, c)}")
