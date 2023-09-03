#Função cachorropeso()
def cachorro_peso():

   while True:
        try:
            peso = float(input("Digite o peso do cachorro (em kg): "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Infelizmente só aceitamos cachorros até 50KG. Tente novamente.")
        except ValueError:
                print("Valor não existente. Por favor digite novamente.")
#Fim da função cachorro_peso

#Função cachorro_pelo
def cachorro_pelo():

    while True:
        pelo = input("Digite qual o tipo de pelo do cachorro (c/m/l): ").lower()
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Tente novamente.")
#Função cachorro_extra ( para serviços adicionais/extra)
def cachorro_extra():
    valor_extra = 0
    while True:
        try:
            adicional = int(input("Escolha o serviço adicional: (0 - Nenhum, 1 - Cortar unhas, 2 - Escovar dentes, 3 - Limpar orelhas): "))
            if adicional == 0:
                break
            elif adicional == 1:
                valor_extra += 10
            elif adicional == 2:
                valor_extra += 12
            elif adicional == 3:
                valor_extra += 15
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Valor não existente. Por favor digite novamente.")
    return valor_extra
#Função Main (Função principal do programa com os multiplicadores de valor indicados no enunciado)
def main():
    print('Bem-vindo(a) ao Pet Shop Banho & Tosa de Gabriel Oliveira Centeno')
    nome = input("Digite o seu nome: ")
    print("Olá,", nome, 'como poderiamos te ajudar?')

    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()
    total = base * multiplicador + extra
    print("O valor total é de: R$", total)

#Para executar o programa e suas funções
if __name__ == '__main__':
    main()




