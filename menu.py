import operacoes
import this
this.opcao = -1
campo = ""
novoDado = ""
peri = ""
this.codigo = 0

def menu():
    print('\no que deseja fazer?\n\n'
            'escolha uma das opções abaixo:\n\n' +
            '1. cadastrar novo mês\n' +
            '2. inserir novo gasto no mês\n' +
            '3. visualizar dados do mês\n' +
            '4. atualizar dado\n'               +
            '5. excluir dado\n'               +
            '0. sair\n')
    this.opcao = int(input())

def operacao():
    while (this.opcao != 0):
        #try:
            menu()
            if this.opcao == 1:#cadastrar novo mês
                print("digite de forma numérica o mês e o ano referente")
                print("mês:")
                mes = int(input())
                while (mes < 0) or (mes > 12):
                    try:
                        print('digite um número entre 1 e 12.')
                        mes = int(input("mes: "))
                    except ValueError:
                        print('digite um número inteiro.')
                print("ano:")
                ano = int(input())
                while (ano < 1500) or (ano > 3500):
                    try:
                        print('digite um número entre 1500 e 3500.')
                        ano = int(input())
                    except ValueError:
                        print('digite um número válido.')
                codigo = "{}{}".format(mes, ano)
                mesAno = "{}/{}".format(mes, ano)
                print("dados digitados estão corretos?")
                print("{}".format(mesAno))
                print('\n1. sim\n' +
                      '2. não\n')
                opcao1 = int(input())
                if opcao1 == 1:#sim estao corretos
                    print("digite quanto voce ganhou ou ganhará em {}".format(mesAno))
                    ganho = input()
                    operacoes.inserirMes(codigo, mesAno, ganho)
                elif opcao1 == 2:#nao estao corretos
                    operacao()
                else:
                    print('opção escolhida não é válida!')

            elif this.opcao == 2:#inserir novo gasto no mês
                print("digite o mes e o ano referente ao gasto que deseja inserir")
                mes = int(input("mes: "))
                while (mes < 0) or (mes > 12):
                    try:
                        print('digite um número entre 1 e 12.')
                        mes = int(input("mes: "))
                    except ValueError:
                        print('digite um número inteiro.')
                ano = int(input("ano: "))
                while (ano < 1500) or (ano > 3500):
                    try:
                        print('digite um número entre 1500 e 3500.')
                        ano = int(input())
                    except ValueError:
                        print('digite um número válido.')
                periodo = "{}/{}".format(mes,ano)
                print("digite de forma numérica apenas o dia do gasto:")
                dia = int(input())
                if mes == 2:
                    while (dia < 0) or (dia > 29):
                        try:
                            print('digite um número entre 1 e 29.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                elif mes == 4:
                    while (dia < 0) or (dia > 30):
                        try:
                            print('digite um número entre 1 e 30.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                elif mes == 6:
                    while (dia < 0) or (dia > 30):
                        try:
                            print('digite um número entre 1 e 30.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                elif mes == 9:
                    while (dia < 0) or (dia > 30):
                        try:
                            print('digite um número entre 1 e 30.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                elif mes == 11:
                    while (dia < 0) or (dia > 30):
                        try:
                            print('digite um número entre 1 e 30.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                else:
                    while (dia < 0) or (dia > 31):
                        try:
                            print('digite um número entre 1 e 31.')
                            dia = int(input("dia: "))
                        except ValueError:
                            print('digite um número inteiro.')
                print("digite em que o dinheiro foi gasto:")
                item = input()
                print("digite de forma numérica quanto dinheiro foi gasto:")
                print("favor digitar ponto ao invés da vírgula.")
                valor = input()
                print("digite onde(lugar) foi gasto:")
                onde = input()
                print("digite a forma de pagamento que foi usada:")
                forma = input()
                try:
                    operacoes.inserirGastos(dia, periodo, item, valor, onde, forma)
                except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                    return operacao()

            elif this.opcao == 3:#visualizar gastos/ganhos por mês
                try:
                    operacoes.consultarMes()
                    print('\n1. visualizar detalhes de um determinado mes\n' +
                            '2. retornar ao menu\n')
                    opcao2 = int(input())
                    if opcao2 == 1:#visualizar detalhes de um determinado mes
                        print("digite de forma numérica o mes que deseja visualizar os detalhes")
                        mes = int(input('mes: '))
                        while (mes < 0) or (mes > 12):
                            try:
                                print('digite um número entre 1 e 12.')
                                mes = int(input("mes: "))
                            except ValueError:
                                print('digite um número inteiro.')
                        print("digite de forma numérica o ano que deseja visualizar os detalhes")
                        ano = int(input('ano: '))
                        while (ano < 1500) or (ano > 3500):
                            try:
                                print('digite um número entre 1500 e 3500.')
                                ano = int(input())
                            except ValueError:
                                print('digite um número válido.')
                        peri = "{}/{}".format(mes,ano)
                        operacoes.consultarGastos(peri)
                        operacoes.somarGastos(peri)
                    elif opcao2 == 2:#retornar ao menu
                        operacao()
                    else:
                        print('opção escolhida não é válida!')
                except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                    return operacao()

            elif this.opcao == 4:#atualizar dado
                print("deseja atualizar quais dados?")
                print('\n1. dados de mês (apenas para atualizar ganho)\n' +
                      '2. dados de gastos\n')
                opcao3 = int(input())
                if opcao3 == 1:#atualizar dados de mês
                    print("digite o código do mes/ano que deseja editar")
                    this.codigo = int(input())
                    campo = 'ganho'
                    print('digite o novo ganho do mes')
                    novoDado = input()
                    try:
                        operacoes.atualizarMes(this.codigo, campo, novoDado)
                    except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                        return operacao()
                elif opcao3 == 2:#atualizar dados de gastos
                    print("digite o código do gasto que deseja editar")
                    this.codigo = int(input())
                    print('digite o número do campo que deseja atualizar')
                    print('\n1. dia do gasto\n' +
                          '2. periodo\n' +
                          '3. item\n' +
                          '4. valor\n' +
                          '5. onde\n' +
                          '6. forma de pagamento')
                    opcao5 = int(input())
                    if opcao5 == 1:#dia
                        campo = 'dia'
                        print('digite o novo {}'.format(campo))
                        novoDado = input()
                    elif opcao5 == 2:#periodo
                        campo = 'periodo'
                        print('digite o novo {}'.format(campo))
                        print('mes:')
                        mes = int(input())
                        print("ano:")
                        ano = int(input())
                        novoDado = "{}/{}".format(mes, ano)
                    elif opcao5 == 3:#item
                        campo = 'item'
                        print('digite o novo dado para atualizar {}'.format(campo))
                        novoDado = input()
                    elif opcao5 == 4:#valor
                        campo = 'valor'
                        print('digite o novo dado para atualizar {}'.format(campo))
                        novoDado = input()
                    elif opcao5 == 5:#onde
                        campo = 'onde'
                        print('digite o novo dado para atualizar {}'.format(campo))
                        novoDado = input()
                    elif opcao5 == 6:#forma de pagamento
                        campo = 'forma'
                        print('digite o novo dado para atualizar forma de pagaemnto')
                        novoDado = input()
                    else:
                        print('opcao inválida')
                    try:
                        operacoes.atualizarGastos(this.codigo, campo, novoDado)
                    except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                        return menu()
                else:
                    print('opção escolhida não é válida!')

            elif this.opcao == 5:#excluir dado
                print("deseja excluir quais dados?")
                print('\n1. dados de mês\n' +
                      '2. dados de gastos\n')
                opcao4 = int(input())
                if opcao4 == 1:#excluir dados de mês
                    print("digite o código do mes que deseja excluir")
                    this.codigo = int(input())
                    try:
                        operacoes.excluirMes(this.codigo)
                    except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                        return menu.operacao()
                elif opcao4 == 2:#excluir dados de gastos
                    print("digite o código do gasto que deseja excluir")
                    this.codigo = int(input())
                    try:
                        operacoes.excluirGastos(this.codigo)
                    except print("nao existem dados para serem exibidos ou dados digitados estao incorretos"):
                        return operacao()
                else:
                    print('opção escolhida não é válida!')

            else:
                print('opção escolhida não é válida!')



