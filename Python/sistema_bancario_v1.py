def main():
    while True:
        opcao = int(input("""
BANCO DO BRASIO
         
[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Cancelar
                          
Opção: """))
        
        match(opcao):
            case 0:
                print("Volte Sempre!")
                return

            case 1:
                valor = float(input('Qual valor deseja depositar? '))
                depositar(valor)

            case 2:
                valor = float(input('Qual valor deseja sacar? '))
                sacar(valor)

            case 3:
                extrato()

            case _:
                print('Opção Inválida!')

def depositar(x):
    global conta
    global extratos
    if x > 0:
        conta += x
        string = f'Depósito: R${x:.2f}'
        extratos.append(string)
        return
    print('Valor inválido, por favor digite um número maior que zero.')
    return

def sacar(x):
    global conta
    global extratos
    global saque_diario
    LIMITE = 500
    if saque_diario == 3:
        print('O limite diário de saque (3x) já foi atingido.')
        return
    elif x > LIMITE:
        print('O saque é maior que o valor permitido por saque (R$500).')
        return
    elif x > conta:
        print('Saldo insuficiente.')
        return
    elif x < 0:
        print('Valor deve ser maior que zero.')
        return
    elif x <= conta:
        conta -= x
        string = f'Saque: R${x:.2f}'
        extratos.append(string)
        saque_diario += 1
        return
    else:
        print('Operação não permitida.')

def extrato():
    global conta
    global extratos
    print(' EXTRATO '.center(29,'='))
    if not extratos:
        print('Ainda não foram feitas movimentações nessa conta.')
    else:
        for extrato in extratos:
            print(extrato)
    print();print()
    print(f'Total: R${conta:.2f}')
    print('='*29)

if __name__ == '__main__':
    conta = 0
    extratos = []
    saque_diario = 0
    main()
    print(conta)
    print(extratos)