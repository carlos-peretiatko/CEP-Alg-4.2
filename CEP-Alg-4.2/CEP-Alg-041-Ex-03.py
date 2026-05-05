# Tabela de conversão de temperaturas. Escreva um programa Python que mostre uma tabela
# de conversão de temperaturas em graus Celsius e graus Fahrenheit. A tabela deve incluir em
# suas linhas todas as temperaturas entre 0 e 100 graus Celsius que sejam múltiplas de 10
# graus Celsius. Inclua os cabeçalhos apropriados e tabulações para suas colunas. Pesquise na
# internet sobre a fórmula de conversão de temperaturas Celsius para Fahrenheit.

# Dica: dentro das strings na função print você pode usar o caracter especial “\t”, que insere
# um espaço de tabulação na string (equivalente a usar a tecla “tab” quando digitamos um
# texto).

print(f"{'Celsius':>10} {'Fahrenheit':>12}")

for c in range(0, 101, 10):
    f = c * 9/5 + 32
    print(f"{c:>10} {f:>12.2f}")