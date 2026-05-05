# Binário para decimal. Escreva um programa Python que converte um número binário (base 2) para
# decimal (base 10). Seu programa deve iniciar lendo um número binário como uma string. Então, ele
# deve computar o número decimal equivalente processando cada dígito do número binário. Finalmente
# seu programa deve exibir uma mensagem informando o número decimal calculado.

binario = input("Digite um número binário: ").strip()

decimal = 0
potencia = 0

# percorre do último dígito para o primeiro
for bit in reversed(binario):
    if bit not in "01":
        print("Erro: o número não é binário.")
        exit()

    if bit == "1":
        decimal += 2 ** potencia

    potencia += 1

print(f"Valor decimal: {decimal}")