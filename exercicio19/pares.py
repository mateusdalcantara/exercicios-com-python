#lista de números
numeros = [1, 2, 3, 4, 5, 6]  
# Usando função lambda com o filter para selecionar números pares
pares = filter(lambda x: x % 2 == 0, numeros)   
# Convertendo o resultado para uma lista
lista_pares = list(pares) 
#imprimir a lista de pares
print(lista_pares)
