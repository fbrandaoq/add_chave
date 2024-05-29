# dicionário

pessoa = {
    'Nome':'Fábio Brandão',
    'Idade':44,
    'Profissão':'Analista',
}

# adicionando nova chave
pessoa['Empresa'] = 'SENAI'

# alterar nome de chave
nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo: ')
pessoa[nova_chave] = novo_valor


#exibe os dados
for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

