#e_087.py
# Dada uma estrutura inicial de um carrinho de compras com 5 itens e seus respectivos valores, 
# assim como uma função que soma os valores dos itens do carrinho, 
# retornando um valor total. aprimore a função deste código usando list comprehension..

carrinho = []
carrinho.append(('prod1', 30))
carrinho.append(('prod2', 45))
carrinho.append(('prod3', 22))
carrinho.append(('prod4', 93))
carrinho.append(('prod5', 6))

total = 0 

lc = sum([carro + total for x,carro in carrinho])

print(f'O total é de: R$ {lc}')

 