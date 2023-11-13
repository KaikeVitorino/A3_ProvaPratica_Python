from HistoricoUtil import * # Importando o modulo das classes criadas por mim
import random # Importando o modulo random para gerar o numero da conta dos clientes

# Criando funcao do Menu
def menu():
    print(f"A) Adicionar cliente\n"
          f"B) Logar usuario\n")

    escolha1 = input("\nDigite a opcao: ")
    escolha1 = escolha1.lower()

    while escolha1 not in ['a', 'b']:
        print("Opcao invalida. Tente novamente.\n")
        escolha1 = input("Digite a opcao: ")

    return escolha1

def menu_2(escolha1):
    # Declarando variaveis essenciais
    nome = None
    cpf = None
    saldo = float()
    n_conta = random.randint(100000000, 999999999)

    conta = Conta(Cliente, Historico, n_conta, saldo)

    if escolha1 == 'a':
        escolha = escolha1
        return escolha

    else:
        conta.ler_procurar_arq_conta()
        print(f"1) Ver infos dos clientes\n"
              f"2) Ver infos das contas dos clientes\n"
              f"3) Depositar\n"
              f"4) Sacar\n"
              f"5) Transferir\n"
              f"6) Ver historico de movimentacao da conta\n"
              f"7) Salvar historico de movimentacao\n"
              f"8) Sair do Programa")

        escolha2 = input("\nDigite a opcao: ")

        while escolha2 not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Opcao invalida. Tente novamente.\n")
            escolha2 = input("Digite a opcao: ")
        return escolha2

def main():

    #Declarando variaveis essenciais
    nome = None
    cpf = None
    saldo = float()
    n_conta = random.randint(100000000, 999999999)

    cliente = Cliente(nome, cpf)
    conta = Conta(Cliente, Historico, n_conta, saldo)
    historico = Historico()

    while True:
        escolha1 = menu()
        escolha2 = menu_2(escolha1)

        if escolha2 == 'a':
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            saldo = float(input("Saldo disponivel na conta do cliente: "))
            print(f"Numero da conta do cliente: {n_conta} \n")

            cliente = Cliente(nome, cpf)
            conta = Conta(Cliente, Historico, n_conta, saldo)

            cliente.gravar_cliente()
            conta.gravar_conta(nome, cpf)

        elif escolha2 == '1':
            cliente.ler_arq_cli()

        elif escolha2 == '2':
            conta.printar_arq_conta()

        elif escolha2 == '3':
            print("Escolha a pessoa para quem eh destinada o deposito.")
            conta.printar_arq_conta()
            destino = input("Digite o nome do destinatario do deposito: ")
            valor = float(input("Valor a ser depositado: \n"))
            conta.deposita(valor, destino)

        elif escolha2 == '4':
            print("Escolha a conta de quem vai ser sacado o valor.")
            conta.printar_arq_conta()
            destino = input("Digite o nome do destinatario do saque: ")
            valor = float(input("Valor a ser sacado: \n"))
            conta.saca(valor, destino)

        elif escolha2 == '5':
            print("Da conta de quem sera realizado a transferencia?")
            conta.printar_arq_conta()
            nome = input("Digite o nome do titular da conta que realizara  a transferencia: ")
            print(f"\nEscolha a pessoa para quem eh destinada a transferencia.")
            cliente.ler_arq_cli()
            destino = input("Digite o nome do destinatario da transferencia: ")
            valor = float(input("Valor a ser transferido: "))

            conta.transferencia_para(valor, nome, destino)

        elif escolha2 == '6':
            historico.imprime()

        elif escolha2 == '7':
            historico.gravaHistorico()

        else:
            print("Encerrando programa...")
            break