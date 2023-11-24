import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        with open('historico.txt', 'r') as f:
            print('========| Historico de movimentacao |========')
            print(f.read())

    def gravaHistorico(self, transacao):
        with open('historico.txt', 'a') as arq:
            arq.write(transacao + '\n')
            self.transacoes.append(transacao)


class Cliente:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def gravar_cliente(self):
        with open('Clientes.txt', 'a') as arq_cli:
            arq_cli.write(f" Nome: {self.nome}\n"
                          f" CPF: {self.cpf}\n"
                          f"|================================|\n")

    def ler_arq_cli(self):
        with open('Clientes.txt', 'r') as f:
            print('|======| Leitura de cliente |======|')
            print(f.read())


class Conta(Cliente):
    def __init__(self, nome, cpf, n_conta, saldo):
        super().__init__(nome, cpf)
        self.n_conta = n_conta
        self.saldo = saldo
        self.historico = Historico()  # Crie uma instância de Historico

    def gravar_conta(self):
        with open('Contas.txt', 'a') as arq_cli:
            arq_cli.write(f"|================================|"
                          f"\n Nome: {self.nome}\n"
                          f" CPF: {self.cpf}\n"
                          f" Numero da conta: {self.n_conta}\n"
                          f" Saldo da conta: {self.saldo}\n")

    def printar_arq_conta(self):
        with open('Contas.txt', 'r') as f:
            print('=====| Lista das contas |=====')
            print(f.read())

    def depositar(self, valor):
        self.saldo += valor
        self.historico.gravaHistorico(f'Depósito de {valor}')

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.gravaHistorico(f'Saque de {valor}')
            return True

    def transferir(self, destino, valor):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico.gravaHistorico(f'Transferência de {valor} para conta {destino.n_conta}')
