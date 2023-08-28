km = int(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))

precodia = 60 * dias
precokm = km * 0.15

final = precodia + precokm

print('O carro rodou {}km por {} dias alugados. Dia = R$60,00 - KM = R$0,15' .format(km, dias))
print('O preço a pagar pelo uso do carro alugado é de R${}.' .format(final))