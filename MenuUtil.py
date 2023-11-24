from HistoricoUtil import *
import random

def menu():
    while True:

        with open('Contas.json', 'r') as arq_contas:
            contas_data = json.load(arq_contas)
            contas = {n_conta: Conta(data['nome'], data['cpf'], n_conta, data['saldo']) for n_conta, data in
                      contas_data.items()}

        clientes = {}

        print("\nMenu:")
        print("A) Adicionar cliente")
        print("B) Ver infos dos clientes")
        print("C) Ver infos das contas dos clientes")
        print("D) Depositar")
        print("E) Sacar")
        print("F) Transferir")
        print("G) Ver historico de movimentacao da conta")
        print("H) Sair do Programa")
        opcao = input("Escolha uma opção: ")

        if opcao.upper() == 'A':
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            numero_aleatorio = random.randint(0, 99999)
            n_conta = f"{numero_aleatorio:05}"
            saldo = float(input("Digite saldo na conta do cliente: "))

            cliente = Cliente(nome, cpf)
            cliente.gravar_cliente()
            clientes[cpf] = cliente

            conta = Conta(nome, cpf, n_conta, saldo)
            conta.gravar_conta()

        elif opcao.upper() == 'B':
            Cliente.ler_arq_cli()

        elif opcao.upper() == 'C':
            Conta.printar_arq_conta()

        elif opcao.upper() == 'D':
            Conta.printar_arq_conta()
            n_conta = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a depositar: "))

            if n_conta in contas:
                contas[n_conta].depositar(valor)
            else:
                print("Conta não encontrada.")

        elif opcao.upper() == 'E':
            Conta.printar_arq_conta()
            n_conta_numero = input("Digite o número da conta: ")
            valor = float(input("Digite o valor a sacar: "))
            # Verifica se a conta existe no dicionário contas
            if n_conta_numero in contas:
                conta_sacar = contas[n_conta_numero]
                # Chama o método sacar da conta correspondente
                if conta_sacar.sacar(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente para realizar o saque.")
            else:
                print("Conta não encontrada.")

        elif opcao.upper() == 'F':
            Conta.printar_arq_conta()
            n_conta_origem = input("Digite o número da conta de origem: ")
            n_conta_destino = input("Digite o número da conta destino: ")
            valor = float(input("Digite o valor a transferir: "))
            # Verifica se as contas de origem e destino existem no dicionário contas
            if n_conta_origem in contas and n_conta_destino in contas:
                n_conta = n_conta_destino
                contas[n_conta_origem].transferir(contas[n_conta_destino], valor)
            else:
                print("Conta de origem ou destino não encontrada.")


        elif opcao.upper() == 'G':
            print('|=======================| Histórico de movimentação |=======================|')
            for conta in contas.values():
                conta.historico.imprime()

        elif opcao.upper() == 'H':
            print("Encerrando programa...")
            break

        else:
            print("Insira alguma opcao valida!")