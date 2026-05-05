# Cara ou coroa. Qual é o menor número de vezes que você precisa sortear uma moeda para
# ter três resultados consecutivos iguais de cara ou de coroa? Qual é o número máximo de
# sorteios necessários? Quantos sorteios precisamos em média? Neste exercício vamos
# explorar estas questões criando um programa que simula várias séries de sorteios de cara ou
# coroa.
# Crie um programa que utilize o gerador de números randômicos do Python para simular o
# sorteio de uma moeda várias vezes. A moeda simulada deve ser justa, ou seja, deve ter a
# mesma probabilidade de gerar cara e coroa. Seu programa deve continuar simulando sorteios
# até que ocorra uma sequencia de 3 caras ou de 3 coroas consecutivas. Exiba A para cada vez
# que ocorrer cara e O para cada vez que ocorrer coroa, com todos os resultados sendo
# exibidos na mesma linha. Então exiba a quantidade de sorteios que levou para chegar a três
# resultados iguais consecutivos. Quando seu programa executar, ele deve fazer esta simulação
# 10 vezes e, ao final, mostrar a quantidade média de sorteios necessária. Abaixo segue um
# exemplo de saída do programa:
# A O O O (4 sorteios)
# A A O O A O A O O A A O A O O A O O O (19 sorteios)
# O O O (3 sorteios)
# O A A A (4 sorteios)
# A A A (3 sorteios)
# O A O O A O A A O O A A O A O A A A (18 sorteios)
# A O O A A A (6 sorteios)
# A O A A A (5 sorteios)
# O O A O O A O A O A A A (12 sorteios)
# O A O O O (5 sorteios)
# Na média, foram necessários 7.9 sorteios.

import random

def simular():
    sequencia = []
    contador = 0

    while True:
        # 0 = cara (A), 1 = coroa (O)
        resultado = random.randint(0, 1)

        if resultado == 0:
            sequencia.append("A")
        else:
            sequencia.append("O")

        contador += 1

        # verifica os últimos 3 resultados
        if len(sequencia) >= 3:
            if sequencia[-1] == sequencia[-2] == sequencia[-3]:
                break

    print(" ".join(sequencia), f"({contador} sorteios)")
    return contador


# 10 simulações
total = 0

for _ in range(10):
    total += simular()

media = total / 10

print(f"\nNa média, foram necessários {media:.1f} sorteios.")