from time import sleep
def main(saldo,historico,limite_diario,users,contas,numero_conta):
    while True:
        print()
        print()
        print()
        opcao = int(input("""
BANCO DO BRASIO
         
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Criar Usuário
[5] - Criar Conta Corrente
[6] - Listar Contas Correntes
[0] - Cancelar
                          
Opção: """))
        
        match(opcao):
            case 0:
                print("Volte Sempre!")
                sleep(1.5)
                return saldo,historico,limite_diario,users,contas,numero_conta

            case 1:
                valor = float(input('Qual valor deseja depositar? '))
                saldo,historico = depositar(valor,saldo,historico)

            case 2:
                valor = float(input('Qual valor deseja sacar? '))
                saldo,historico,limite_diario = sacar(valor=valor,saldo=saldo,historico=historico,limite_diario=limite_diario)

            case 3:
                extrato(saldo,historico=historico)

            case 4:
                nome = input("Nome: ")
                data = input("Data de nascimento (dd-mm-aaaa): ")
                cpf = input("CPF: ")
                endereco = input("Endereço (Rua, nº - bairro - cidade/UF): ")

                valor = criar_usuario(users,nome=nome,data=data,cpf=cpf,endereco=endereco)
                if valor is not None:
                    users.append(valor)

            case 5:
                cpf = input('CPF: ')
                numero_conta,valor = criar_conta_corrente(numero_conta=numero_conta,cpf=cpf,usuarios=users)
                if valor is not None:
                    contas.append(valor)

            case 6:
                listar_contas(contas)


            case _:
                print('Opção Inválida!')

def depositar(valor,saldo,historico,/):
    # global conta
    # global extratos
    if valor > 0:
        saldo += valor
        string = f'Depósito: R${valor:.2f}'
        historico.append(string)
        return saldo,historico
    print('Valor inválido, por favor digite um número maior que zero.')
    sleep(1.5)
    return saldo,historico

def sacar(valor,saldo,historico,limite_diario):
    # global conta
    # global extratos
    # global saque_diario
    LIMITE = 500
    if limite_diario == 3:
        print('O limite diário de saque (3x) já foi atingido.')
        sleep(1.5)
        return saldo,historico,limite_diario
    if valor > LIMITE:
        print('O saque é maior que o valor permitido por saque (R$500).')
        sleep(1.5)
        return saldo,historico,limite_diario
    if valor > saldo:
        print('Saldo insuficiente.')
        sleep(1.5)
        return saldo,historico,limite_diario
    if valor < 0:
        print('Valor deve ser maior que zero.')
        sleep(1.5)
        return saldo,historico,limite_diario
    if valor <= saldo:
        saldo -= valor
        string = f'Saque: R${valor:.2f}'
        historico.append(string)
        limite_diario += 1
        return saldo,historico,limite_diario
    print('Operação não permitida.')
    sleep(1.5)
    return saldo,historico,limite_diario

def extrato(saldo,/,historico):
    
    # global conta
    # global extratos
    print(' EXTRATO '.center(29,'='))
    if not historico:
        print('Ainda não foram feitas movimentações nessa conta.')
    else:
        for linha in historico:
            print(linha)
    print()
    print()
    print(f'Total: R${saldo:.2f}')
    print('='*38)
    input('Pressione enter ao terminar de ler ')

def criar_usuario(*args,**kwargs):
    if args[0]:
        for dic in args[0]:
            if dic["cpf"] == kwargs["cpf"]:
                print("CPF já cadastrado. Encerrando criação de usuário...")
                sleep(1.5)
                return None
    print()
    print()
    print(f'Usuário {kwargs["nome"]} cadastrado com sucesso!')
    sleep(1.5)
    return kwargs

def criar_conta_corrente(numero_conta,cpf,usuarios):
    AGENCIA = '0001'
    nome = ''
    if usuarios:
        for user in usuarios:
            if user['cpf'] == cpf:
                nome = user['nome']
                break
            else:
                continue
        if not nome:
            print('CPF não cadastrado. Encerrando abertura de conta...')
            sleep(1.5)
            return numero_conta, None
        valor = {'agencia': AGENCIA,
                'nome':nome,
                'numero_conta':numero_conta
                }
        numero_conta += 1
        print(f'Conta criada para {nome} de CPF {cpf}')
        sleep(1.5)
        return numero_conta, valor

    print('Sem usuários cadastrados. Encerrando abertura de conta...')
    sleep(1.5)
    return numero_conta,None

def listar_contas(contas):
    print(' CONTAS '.center(30,'='))
    if not contas:
        print('Não foram criadas contas até o momento.')
    else:
        for linha in contas:
            print(
    f"""
        A/C: {linha['agencia']}
        C/C: {linha['numero_conta']}
        nome: {linha['nome']}


    """)
    print('='*38)
    input('Pressione enter ao terminar de ler ')



if __name__ == '__main__':
    conta = 0
    saque_diario = 0
    numero_conta = 1
    extratos = []
    usuarios = []
    contas_correntes = []
    conta,extratos,saque_diario,usuarios,contas_correntes,numero_conta = main(saldo=conta,historico=extratos,limite_diario=saque_diario,users=usuarios,contas=contas_correntes,numero_conta=numero_conta)
    