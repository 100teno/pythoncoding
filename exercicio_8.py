nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome == 'Gabriel':
    print('Olá, Gabriel!')
elif(idade<18):
    print('Você não é o Gabriel! E é menor de idade.')
elif(idade>=100):
    print('Diferente de você, o Gabriel não é imortal!')