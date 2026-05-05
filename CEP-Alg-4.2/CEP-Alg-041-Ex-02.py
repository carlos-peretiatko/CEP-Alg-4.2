# Tabela de descontos. Uma loja está oferecendo uma liquidação com descontos de 60% em
# uma variedade de produtos em final de estoque. O vendedor gostaria de ajudar seus clientes a
# determinar o preço reduzido (com desconto) de seus produtos. Ele quer criar uma tabela que
# mostra os preços originais e os preços após o desconto ser aplicado. Escreva um programa
# Python usando laço de repetição que gere esta tabela mostrando o preço original, o valor de
# desconto e o novo valor com desconto aplicado para produtos com os seguintes valores:
# R$ 4.95, R$ 9.95, R$ 14.95, R$ 19.95 e R$ 24.95. Certifique-se que todos os valores são
# mostrados com duas casas decimais.

precos = [4.95, 9.95, 14.95, 19.95, 24.95]
descontoPer = 0.60 #60%

print(f"{'Preço Original':>15} {'Desconto':>15} {'Preço Final':>15}")

for preco in precos:
    desconto = preco * descontoPer
    final = preco - desconto

    print(f"R$ {preco:>10.2f} R$ {desconto:>10.2f} R$ {final:>10.2f}")