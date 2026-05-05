# 13. Fatoração numérica. A fatoração de um número inteiro n pode ser feita por meio de números
# primos de acordo com o procedimento descrito abaixo:
# Inicialize fator com valor 2
# Enquanto fator for menor ou igual a n, faça
# Se n for divisível por fator então
# Concluímos que fator faz parte da fatoração de n
# Faça divisão inteira de n por fator
# Senão
# Incremente fator em uma unidade
# Escreva um programa Python que lê um número inteiro do usuário. Se o valor fornecido pelo
# usuário é menor do que 2, seu programa deve exibir uma mensagem de erro. Caso contrário,
# seu programa deve exibir os números primos que podem ser multiplicados para formar o
# número n, com um fator exibido em cada linha. Por exemplo:
# Digite um número inteiro (maior ou igual a 2): 72
# 2
# 2
# 2
# 3
# 3

n = int(input("Digite um número inteiro (maior ou igual a 2): "))

if n < 2:
    print("Erro: o número deve ser maior ou igual a 2.")
else:
    fator = 2

    while fator <= n:
        if n % fator == 0:
            print(fator)
            n = n // fator
        else:
            fator += 1