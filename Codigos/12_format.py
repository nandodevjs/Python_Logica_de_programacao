a = 'A'
b = 'B'
c = 1.5

formato = 'a{}, b{}, c{}'.format(a, b, c)

# Posso passar como índice também
formato = 'a{0}, b{2}, c{1}'.format(a, b, c)

print(formato)