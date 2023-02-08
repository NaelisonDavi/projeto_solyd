idade = int(input('insira a idade: '))
peso = int(input('insira o peso: '))
altura = float(input('insira a altura: '))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print('aprovado')
else:
    print('reprovado')
