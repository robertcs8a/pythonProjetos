# procura se tem o nome especifidao na string (city)
# metodo usado fatiamento de caracteres 

#localizar o nome "Santo" no inicio do Nome das Cidades Informadas
city = str(input('Informe o nome da Cidade : ')).upper().strip()
print(city)

print( city[:5] == 'santo')
