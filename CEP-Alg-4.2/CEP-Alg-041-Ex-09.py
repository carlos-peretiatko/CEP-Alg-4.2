# Raiz quadrada. Escreva um programa Python que implemente o método de Newton para
# calcular e exibir o valor da raiz quadrada de um número. O método de Newton é descrito pelo
# pseudo-código abaixo:
# Leia o valor de x do usuário
# Inicialize raiz = x/2
# Enquanto raiz não é boa o suficiente, faça
# Atualize raiz para receber a média entre raiz e x/raiz
# Quando o algoritmo chega ao fim, raiz contém um valor aproximado da raiz quadrada de x. A
# qualidade desta aproximação depende de como você define “boa o suficiente”. Podemos, por
# exemplo, considerar a solução boa o suficiente quando o valor absoluto da diferença entre
# raiz * raiz e x é menor que 10^-12.

x = float(input("Digite um número: "))

raiz = x / 2.0
tolerancia = 1e-12

# evita erro para x = 0
if x == 0:
    raiz = 0
else:
    while abs(raiz * raiz - x) > tolerancia:
        raiz = (raiz + x / raiz) / 2

print(f"Raiz aproximada de {x} = {raiz}")