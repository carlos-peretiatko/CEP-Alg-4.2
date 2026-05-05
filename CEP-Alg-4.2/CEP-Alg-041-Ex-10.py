# Palíndromo. Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica
# à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando
# laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um
# palíndromo. Seu programa deve exibir uma mensagem informando o resultado.

palavra = input("Digite uma palavra: ").strip()

ehPalindromo = True
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - 1 - i]:
        ehPalindromo = False
        break

if ehPalindromo:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")