""" upper(): converte todos os caracteres da string em maiúsculas.
lower(): converte todos os caracteres da string em minúsculas.
split(): divide a string em uma lista de substrings com base no separador especificado.
join(): junta uma lista de strings em uma única string com base no separador especificado.
replace(): substitui todas as ocorrências de um caractere ou substring por outra.
capitalize(): retorna uma cópia da string com a primeira palavra iniciando em maiúscula, e as demais letras minúsculas.
title(): Retorna uma cópia da string com todas as palavras iniciando em maiúscula, e as demais letras minúsculas."""
nome = input('digite nome completo : ')
print(f'quantidade de letras da variavel = { (len(nome))}')

print(f'muda todas as letras para maiuscula = {nome.upper()}')

print(f'muda todas as letra para minusculas = {nome.lower()}')

print(f"Quantidade de letras sem considerar espaços = {len(nome.replace(" ", ""))}")

print(f"Quantidade de letras que tem o primeiro nome = { len(nome.split()[0])}")

