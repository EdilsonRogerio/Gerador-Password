import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Seja Bem Vindo ao PyPassword Generator!")
nr_letras= int(input("Quantas letras gostaria de colocar no seu senha?\n")) 
nr_simbolos = int(input(f"Quantos simbolos?\n"))
nr_numeros = int(input(f"Quantos simbolos?\n"))

# senha = ""
# for char in range(1, nr_letras + 1):
#     random_char = random.choice(letras)
#     senha += random_char

# for char in range(1, nr_simbolos + 1):
#     simbolo_aleatorio = random.choice(simbolos)
#     senha += simbolo_aleatorio

# for char in range(1, nr_numeros + 1):
#     numero_aleatorio = random.choice(numeros)
#     senha += numero_aleatorio

# print(senha)

lista_senhas = []
for char in range(1, nr_letras + 1):
    lista_senhas.append(random.choice(letras))

for char in range(1, nr_simbolos + 1):
    lista_senhas += random.choice(simbolos)

for char in range(1, nr_numeros + 1):
    lista_senhas += random.choice(numeros)

print(lista_senhas)
random.shuffle(lista_senhas)
print(lista_senhas)

senha = ""
for char in lista_senhas:
    senha += char

print(senha)
