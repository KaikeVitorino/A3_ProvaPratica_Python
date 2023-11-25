from HistoricoUtil import *
import random
'''
    Modulo onde se tem a func do menu, q eh a principal
        Aqui se aplica logica às classes criadas no outro modulo e ao Menu criado aqui
            A funcao junta os dois fazendo o programa funcionar
'''
# Func que da o menu - a principal
def menu():
    while True:

        # Carrega o arquivo das cotnas em um dicionario
        with open('Contas.json', 'r') as arq_contas:
            contas_data = json.load(arq_contas)
            contas = {n_conta: Conta(data['nome'], data['cpf'], n_conta, data['saldo']) for n_conta, data in
                      contas_data.items()}

        # Dicionario vazio para por os clientes antes do arquivo
        clientes = {}

        # Exibe o menu
        print("\nMenu:")
        print("A) Adicionar cliente")
        print("B) Ver infos dos clientes")
        print("C) Ver infos das contas dos clientes")
        print("D) Depositar")
        print("E) Sacar")
        print("F) Transferir")
        print("G) Ver historico de movimentacao da conta")
        print("H) Sair do Programa")
        opcao = input("Escolha uma opção: ")  # Input para usuario por a opcao

        # Executa a opcoa escolhida
        if opcao.upper() == 'A':  # Adiciona cliente
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            numero_aleatorio = random.randint(0, 99999)  # Gera um numero aleatorio para a conta
            n_conta = f"{numero_aleatorio:05}"  # Formata o numero da conta para ter a mesta quantidade de caracteres q os outros
            saldo = float(input("Digite saldo na conta do cliente: "))

            cliente = Cliente(nome, cpf)  # Cria um novo cliente
            cliente.gravar_cliente()  # Grava o cliente no arquivo
            clientes[cpf] = cliente  # add o cliente no dicionario

            conta = Conta(nome, cpf, n_conta, saldo)  # Cria uma nova conta
            conta.gravar_conta()  # Grava a conta no arquivo

        elif opcao.upper() == 'B':  # Ver informacoes dos clientes
            Cliente.ler_arq_cli()  # da print no arquivo de clientes

        elif opcao.upper() == 'C':  # Ver informacoes das contas dos clientes
            Conta.printar_arq_conta()  # da pirnt no arquiv das contas

        elif opcao.upper() == 'D':  # Depositar
            Conta.printar_arq_conta() # printa todas as contas para vc ver o numero das contas
            n_conta = input("Digite o número da conta: ")  # Escolhe o numero da conta para onde vai depositar
            valor = float(input("Digite o valor a depositar: "))  # Fala o valor do deposito

            # Verifica se a conta existe
            if n_conta in contas:
                contas[n_conta].depositar(valor)  # Deposita o valor na conta
            else:
                print("Conta não encontrada.")  # da print dizendo que nn achou a conta

        elif opcao.upper() == 'E':  # Sacar
            Conta.printar_arq_conta()  # printa todas as contas para vc ver o numero das contas
            n_conta_numero = input("Digite o número da conta: ")  # Input do usuariio do numero da ocnta
            valor = float(input("Digite o valor a sacar: "))  # Bota o valor do saque

            # Verfica se a conta com esse numero existe
            if n_conta_numero in contas:
                conta_sacar = contas[n_conta_numero]  # Pega a conta que vc especificou com o n_conta
                # CHama a func que faz o saque
                if conta_sacar.sacar(valor):
                    print("Saque realizado com sucesso!")  # Da print dizendo qyue o saque funcionou
                else:
                    print("Saldo insuficiente para realizar o saque.")  # Da print dizendo que tu ta pobre
            else:
                print("Conta não encontrada.")  # DIz q nn achou a conta

        elif opcao.upper() == 'F':  # Transferir
            Conta.printar_arq_conta()  # Imprime as contas para vc escolher
            n_conta_origem = input("Digite o número da conta de origem: ")  # input do numero da conta que vai ENVIAR o dinheiro
            n_conta_destino = input("Digite o número da conta destino: ")  # input do numero da conta que vai RECEBER o dinheiro
            valor = float(input("Digite o valor a transferir: "))  # Pergunta qual o valor que vc vai transferir

            # Ve se as contas existem
            if n_conta_origem in contas and n_conta_destino in contas:
                n_conta = n_conta_destino
                contas[n_conta_origem].transferir(contas[n_conta_destino], valor)  # Faz a transferencia
            else:
                print("Conta de origem ou destino não encontrada.")  # Da print em um erro falando que nn encontrou alguma das contas

        elif opcao.upper() == 'G':  # Da print no historico de movimentacao das contas
            print('|=======================| Histórico de movimentação |=======================|')
            for conta in contas.values():  # Para todas as contas do dicionarios
                conta.historico.imprime()       # da print no historico

        elif opcao.upper() == 'H':  # Sai do program, ou seja, break
            print("Encerrando programa...")
            break  # Sai do loop

        else:  # Se nn for nenhuma, ele volta para o inicio
            print("Insira alguma opcao valida!")  # Da print falando q a opcao q pois nn vale
