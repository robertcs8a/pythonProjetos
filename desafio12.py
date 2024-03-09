# calculo de porcentagem de desconto de um item
mercadoria = (input('digite um produto : '))
valor = float(input('informe o valor do produto : '))
porcentagem = valor / 100 * 5 - valor
print(f'o produto: {mercadoria} custa :R$ {valor} reais com desconto de 5% paga-se apenas {porcentagem} reais')