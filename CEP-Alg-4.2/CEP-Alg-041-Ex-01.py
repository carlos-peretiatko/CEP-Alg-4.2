# Média aritmética. Escreva um programa Python que calcula a média aritmética de um
# conjunto de valores fornecidos pelo usuário. O usuário deve entrar com o valor 0 indicando
# que não serão mais fornecidos novos valores. Seu programa deve exibir uma mensagem de
# erro se o primeiro valor fornecido pelo usuário for 0.

# Dica: o número 0 não deve ser incluído no cálculo da média, pois ele só serve para sinalizar
# o final da entrada de dados.

numero = float(input("Informe a primeira nota da média: "))

if numero == 0:
    
    print("erro: você não pode fazer média com zero!")
    
else:
    x = 0 #contador
    y = 0 #acumulador
    while numero != 0:
        numero = float(input("Informe mais notas: (0 fecha) "))
        x+=1
        if numero != 0:
            y+=numero
            
    print("média: ", y/x)
        