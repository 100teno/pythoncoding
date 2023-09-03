print('Bem-vindo(a) a Sorveteria do Gabriel Oliveira Centeno')
#Menu de preços e instruções que irá aparecer com print na tela do cliente.
print('-' * 35, 'cardápio', '-' * 35)
print('|', 'N° de bolas', '|', 'Sabor Tradicional (tr)', '|' , 'Sabor Premium (pr)', '|', 'Sabor Especial (es)', '|')
print('|', '    1      ' , '|', '      R$6,00        ', '|' , '     R$7,00       ',  '|', '      R$8,00       ', '|')
print('|', '    2      ' , '|', '      R$11,00       ', '|' , '     R$13,00      ',  '|', '      R$15,00      ', '|')
print('|', '    3      ' , '|', '      R$15,00       ', '|' , '     R$18,00      ',  '|', '      R$21,00      ', '|')
print('-' * 80)

preco = {
    "tr": {"1": 6, "2": 11, "3": 15},
    "pr": {"1": 7, "2": 13, "3": 18},
    "es": {"1": 8, "2": 15, "3": 21}
}

while True:
    sabor = input('Entre com o sabor desejado (tr/pr/es): ')
    if sabor == 'tr' or sabor == 'pr' or sabor == 'es':
        nbolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
        if nbolas == '1' or nbolas == '2' or nbolas == '3':
            if nbolas == 1:
                if sabor == 'tr':
                    valortotal = 6.00
                elif sabor == 'pr':
                    valortotal = 7.00
                elif sabor == 'es':
                    valortotal = 8.00
            elif nbolas == '2':
                if sabor == 'tr':
                    valortotal = 10.00
                elif sabor == 'pr':
                    valortotal = 12.00
                elif sabor == 'es':
                    valortotal = 14.00
            elif nbolas == '3':
                if sabor == 'tr':
                    valortotal = 14.00
                elif sabor == 'pr':
                    valortotal = 17.00
                elif sabor == 'es':
                    valortotal = 20.00
            maisumpedido = input('Deseja pedir mais algum sorvete (s/n)?')
            if maisumpedido == 's':
                continue
            elif maisumpedido == 'n':
                break
        else:
            print('Número de bolas do sorvete inválido. Tente novamente.')
            continue
    else:
        print('Sabor inválido. Tente novamente.')
        continue
print ('O valor total a ser pago: R${}'.format(valortotal))



