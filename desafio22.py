""" upper(): converte todos os caracteres da string em maiúsculas.
lower(): converte todos os caracteres da string em minúsculas.
split(): divide a string em uma lista de substrings com base no separador especificado.
join(): junta uma lista de strings em uma única string com base no separador especificado.
replace(): substitui todas as ocorrências de um caractere ou substring por outra.
capitalize(): retorna uma cópia da string com a primeira palavra iniciando em maiúscula, e as demais letras minúsculas.
title(): Retorna uma cópia da string com todas as palavras iniciando em maiúscula, e as demais letras minúsculas."""
nome = 'Jose Alencar Silva'
print(len(nome))
nome = nome.upper()  # muda todos caracteres para maiuscula
print(nome)
nome = nome.lower() # muda todos caracteres para minuscula

teste
print(nome)
print("Quantidade de letras sem considerar espaços")
nome_sem_espaco = len(nome.replace(" ", ""))
print(nome_sem_espaco)

print("Quantidade de letras tem o primeiro nome")
primeiro_nome_sem_espaco = len(nome.split()[0])
print(primeiro_nome_sem_espaco)