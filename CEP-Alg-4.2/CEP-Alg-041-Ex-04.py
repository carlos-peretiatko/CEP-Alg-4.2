# Perímetro de um polígono. Crie um programa Python para calcular o perímetro de um
# polígono sendo fornecidas as coordenadas x e y de cada um de seus vértices. Inicie lendo x e
# y do primeiro vértice. Depois disso continue lendo x e y dos próximos vértices até que o
# usuário entre com uma linha em branco para o valor da coordenada x (ou seja, quando ele
# digitar “Enter" ou “Return" sem fornecer um valor). Cada vez que você ler as coordenadas de
# um novo vértice, você deve calcular a distância em relação ao vértice anterior e acrescentá-la
# ao valor do perímetro. A figura abaixo ilustra como se calcula a distância entre dois pontos
# sendo dadas suas coordenadas x e y.

import math

perimetro = 0.0

# leitura do primeiro vértice
xInicial = input("x do primeiro vértice: ").strip()
if xInicial == "":
    print("Nenhum vértice informado.")
    exit()

yInicial = float(input("y do primeiro vértice: "))

xAnterior = float(xInicial)
yAnterior = yInicial

primeiroX = xAnterior
primeiroY = yAnterior

while True:
    xStr = input("x do próximo vértice (Enter para finalizar): ").strip()
    if xStr == "":
        break

    yStr = input("y do próximo vértice: ").strip()

    xAtual = float(xStr)
    yAtual = float(yStr)

    # distância entre pontos
    distancia = math.hypot(xAtual - xAnterior, yAtual - yAnterior)
    perimetro += distancia

    xAnterior = xAtual
    yAnterior = yAtual

# fecha o polígono (último -> primeiro)
perimetro += math.hypot(primeiroX - xAnterior, primeiroY - yAnterior)

print(f"Perímetro do polígono: {perimetro:.2f}")