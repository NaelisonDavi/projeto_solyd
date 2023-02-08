pessoas = []
numero_convidados = -1
nome = ''

while nome != 'sair':
    nome = input('Digite o nome do convidado ou sair para prosseguir: ')
    numero_convidados = numero_convidados + 1
    pessoas.append(nome)
    if nome == 'sair':
        pessoas.pop()
        print('Veja a seguir sua lista completa de convidados:')
        break

for i in pessoas:
    print(f'Nome do convidado: {i}.')

print(f'Você convidou um total de {numero_convidados} pessoas')