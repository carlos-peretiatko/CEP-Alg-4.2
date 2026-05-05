# Aproximação do valor de . O valor aproximado de pode ser calculado pela série infinita
# apresentada abaixo:



# Escreva um programa Python que exiba 15 aproximações de . A primeira aproximação deve
# ter apenas o primeiro termo da série (ou seja, o valor resultante vai ser somente 3). Cada nova
# aproximação de mostrada pelo seu programa deve incluir mais um termo da série, sendo
# cada vez uma aproximação mais precisa do que a anterior.

pi = 3
sinal = 1
i = 2

print(f"1ª aproximação: {pi}")

for n in range(2, 16):
    termo = 4 / (i * (i + 1) * (i + 2))
    pi += sinal * termo

    print(f"{n}ª aproximação: {pi:.10f}")

    sinal *= -1   # alterna + e -
    i += 2        # próximo bloco (2,4,6,...)