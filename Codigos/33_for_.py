"""
Iteravel retorna um valor por vez.

Para cada iterador dentro do iteravel
for ..............   in   ....{...}........ 

A cada iteração do loop, o valor de "elemento" é atualizado para o próximo elemento na sequência, e o bloco de código dentro do loop é executado. O loop continua até que todos os elementos da sequência tenham sido processados.
"""

texto = 'Python'
novo_texto = ''


for i in texto:
    novo_texto += f'*{i}'

    print(i)

print(novo_texto)
