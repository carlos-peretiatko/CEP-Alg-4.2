# Cifra de César. Um dos primeiros exemplos conhecidos de criptografia foi utilizado pelo
# imperador romano Julio César. César precisava fornecer instruções por escrito para seus
# generais, mas não queria que seus inimigos descobrissem suas estratégias caso as
# mensagens com as instruções fossem extraviadas. Com isso, ele acabou desenvolvendo o
# que mais tarde ficou conhecido como a “cifra de César”.
# A idéia por trás desta cifra é simples (e portanto não oferece proteção contra as técnicas
# modernas de quebra de códigos). Cada letra da mensagem original é deslocada em 3
# posições. Com isso, a letra A se torna letra D, B se torna E, C se torna F, e assim por diante. A
# ultimas 3 letras do alfabeto são transformadas nas primeiras. X se torna A, Y se torna B e Z se
# torna C. Caracteres que não são letras não são convertidos.
# Escreva um program Python que implemente a cifra de César. Permita que o usuário forneça a
# mensagem e a distância de deslocamento de letras (portanto não será o valor fixo de
# deslocamento de 3 letras no alfabeto). Certifique-se que seu programa codifique corretamente
# tanto letras maiúsculas quanto minúsculas. Seu programa também deve suportar valores
# negativos de deslocamento de letras, assim ele pode ser usado tanto para codificar quanto
# para decodificar mensagens.

# Dica: você pode usar as funções ord(c) e chr(n) do Python. A função ord(c) retorna um
# número inteiro que representa o caracter Unicode c. A função chr(n) retorna o caracter
# Unicode representado pelo número inteiro n.

def cifra_cesar(texto, deslocamento):
    resultado = ""

    for c in texto:
        if c.isalpha():
            # define base dependendo se é maiúscula ou minúscula
            base = ord('A') if c.isupper() else ord('a')

            # posição da letra no alfabeto (0–25)
            pos = ord(c) - base

            # aplica deslocamento com wrap-around
            novaPos = (pos + deslocamento) % 26

            # volta para caractere
            novoChar = chr(base + novaPos)
            resultado += novoChar
        else:
            # mantém caracteres não alfabéticos
            resultado += c

    return resultado


# uso
mensagem = input("Digite a mensagem: ")
desloc = int(input("Digite o deslocamento: "))

resultado = cifra_cesar(mensagem, desloc)
print("Resultado:", resultado)