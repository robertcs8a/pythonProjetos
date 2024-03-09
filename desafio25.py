#localizar o nome "SILVA" em qualquer nome digitado 
name_s = input('informe um nome para analize : ').strip().upper().lower()
print(f'este nome tem silva ={('silva'in name_s)}')