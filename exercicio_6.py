
nota1 = float(input('Digite a nota de Matemática: '))
nota2 = float(input('Digite a nota de Português: '))
nota3 = float(input('Digite a nota de Ciências: '))

media = (nota1 + nota2 + nota3) / 3

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7:
    print('A sua média final é de {}, você está APROVADO!' .format(media))
else:
    print('A sua média final é de {}, você está REPROVADO!' .format(media))