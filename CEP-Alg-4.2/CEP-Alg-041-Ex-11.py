# Palíndromos com múltiplas palavras. O conceito de palíndromo também pode ser aplicado
# a frases, por exemplo: “A base do teto desaba”. Faça um novo programa Python que
# modifique o programa do exercício anterior para verificar se frases são palíndromos. Seu
# programa vai precisar ignorar os espaços em brando das frases. Como desafio adicional,
# amplie sua solução para que também ignore sinais de pontuação e trate letras maiúsculas e
# minúsculas como equivalentes.

import string

frase = input("Digite uma frase: ")

# remove espaços e pontuação, e coloca tudo em minúsculo
fraseLimpa = ""

for c in frase:
    if c.isalnum():  # mantém apenas letras e números
        fraseLimpa += c.lower()

# verifica se é igual ao reverso
eh_palindromo = True
tamanho = len(fraseLimpa)

for i in range(tamanho // 2):
    if fraseLimpa[i] != fraseLimpa[tamanho - 1 - i]:
        ehPalindromo = False
        break

if ehPalindromo:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")