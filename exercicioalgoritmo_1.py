precoproduto = float (input('Insira o preço do produto: '))
percentual = float (input('Insira o desconto a ser aplicado (0-100%):'))
desconto = precoproduto * (percentual/100)
final= precoproduto - desconto


print('Um desconto de {}% no valor de R${} foi aplicado no produto que custa R${} e o preço final com desconto aplicado é de R${} .'
      .format(percentual, desconto, precoproduto, final))

