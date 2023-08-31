#O programa iniciará com uma mensagem de bem-vindo sendo printada na tela e em seguida irá requisistar os dados necessários, como nome do produto, valor da unidade do produto e a quantidade desejada.
print('Seja Bem-vindo a Loja do Gabriel Oliveira Centeno')
nomep = input('Digite o nome do produto:')
vp = float(input('Digite o valor da unidade do produto: R$'))
qtd = int(input('Digite a quatidade do produto:'))
#O programa irá calcular com a multiplicação das variáveis vp(Valor Produto) e qtd(Quantidade) o valor total sem desconto no produto.
valorsd = vp * qtd

#O programa irá calcular o valor total com desconto no produto.

if qtd < 200: #Se a quantidade de unidades for menor que 200, o desconto será 0.
    desconto = 0

elif qtd < 1000: #Se a quantidade de unidades for maior ou igual 200 e menor que 1000, o desconto será 0.05 = 5%
    desconto = 0.05

elif qtd < 2000:  # Se a quantidade de unidades for maior ou igual 1000 e menor que 2000, o desconto será 0.1 = 10%
    desconto = 0.1

else: #E se a quatidade não for nenhuma das outras opções, e for maior ou igual a 2000, o desconto será de 0.15 = 15%
    desconto = 0.15


#valorsd (Valor sem desconto) vai ser multiplicado pela varíavel criada 'desconto'
valorcd = valorsd * desconto

#Depois dos valores serem inseridos, todas as informações necessariás foram obtidas, agora o programa mostra na tela print das informações obtidas pelas variáveis com input.
print('Nome do produto: {}'.format(nomep))
print('Valor da unidade do produto: R${}'.format(vp))
print('Quantidade do produto: {}' .format(qtd))
print('Total sem o desconto aplicado: R${}'.format(valorsd))
print('Total com o desconto aplicado: R${}'.format(valorsd-valorcd))

#O programa mostra todos os dados inseridos e os valores dos produtos com desconto e sem desconto, assim como pedido no exercício.





