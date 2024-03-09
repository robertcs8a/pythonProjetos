#localizar o nome "SILVA" em qualquer nome digitado 
name_s = input('informe um nome para analize : ').strip().lower()
print(name_s)
print(f'este nome tem silva ={('silva'in name_s)}')