import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        f = open('historico.txt', 'r')
        print('========| Historico de movimentacao |========')
        l = f.read()
        print(f"\n", l)

    def gravaHistorico(self):
        arq = open('historico.txt', 'a')
        historico_str = '\n'.join(self.transacoes)  # Une todas as strings da lista com quebras de linha
        arq.write(historico_str)


class Cliente:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def gravar_cliente(self):
        arq_cli = open('Clientes.txt', 'a')
        arq_cli.write(f" Nome: {self.nome}\n"
                      f" CPF: {self.cpf}\n"
                      f"|================================|\n")

    def ler_arq_cli(self):
        f = open('Clientes.txt', 'r')
        print('|======| Leitura de cliente |======|')
        l = f.read()
        print(f"{l}\n")



class Conta(Cliente):
    def __init__(self, nome, cpf, n_conta, saldo):
        super().__init__(nome, cpf)
        self.n_conta = n_conta
        self.saldo = saldo
        self.historico = Historico()  # Crie uma instância de Historico

    def deposita(self, valor, destino):
        saldoAnterior = self.saldo
        self.nome = destino
        self.saldo += valor
        self.historico.transacoes.append(str(f"\nConta do cliente, {destino}"
                                             f"\n Saldo anterior:{saldoAnterior}"
                                         f"\nDeposito feito no valor feito de {valor}. "
                                         f"\nSaldo atual: {self.saldo}. "
                                         f"\nHorario: {datetime.datetime.today()}"
                                         f"\n|====================================================|"))
        self.historico.gravaHistorico()

    def saca(self, valor, destino):
        saldoAnterior = self.saldo
        self.nome = destino
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(str(f"\nConta do cliente, {destino}"
                                                 f"\n Saldo anterior:{saldoAnterior}"
                                             f"\nRetirada de {valor}. "
                                             f"\nSaldo atual: {self.saldo}. "
                                             f"\nHorario: {datetime.datetime.today()}"
                                             f"\n|====================================================|"))
            self.historico.gravaHistorico()
        else:
            print("Saldo insuficiente.")

    def transferencia_para(self, valor, nome, destino):
        saldoAnterior = self.saldo
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.transacoes.append(str(f"\nConta do cliente, {nome}"
                                                 f"\n Saldo anterior:{saldoAnterior}"
                                                 f"\nTransferência de {valor} para conta de {destino}. "
                                                 f"\nSaldo anterior: {self.saldo}. "
                                                 f"\nHorario: {datetime.datetime.today()}"
                                                 f"\n|====================================================|"))
            self.historico.gravaHistorico()
            Conta.deposita(valor, destino)
        else:
            print("Saldo insuficiente para a transferência.")

    def gravar_conta(self, nome, cpf):
        arq_cli = open('Contas.txt', 'a')
        arq_cli.write(f"|================================|"
                      f"\n Nome: {nome}\n"
                      f" CPF: {cpf}\n"
                      f" Numero da conta: {self.n_conta}\n"
                      f" Saldo da conta: {self.saldo}\n")

    def printar_arq_conta(self):
        f = open('Contas.txt', 'r')
        print('=====| Lista das contas |=====')
        l = f.readlines()
        print(f"{l}\n")

