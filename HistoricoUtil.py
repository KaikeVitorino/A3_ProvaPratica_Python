import datetime
import json

class Historico:
    def __init__(self):
        # Inicializa o historico com a data de abertura e uma lista vazia de transacoes
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        # Imprime o conteudo do historico lido do arquivo 'historico.txt'
        with open('historico.txt', 'r') as f:
            print(f.read())

    def gravaHistorico(self, transacao):
        # Grava a transacao no arquivo 'historico.txt' e adiciona à lista de transacoes
        with open('historico.txt', 'a') as arq:
            arq.write(transacao + '\n')
        print("Gravado no historico!!")
        self.transacoes.append(transacao)


class Cliente:
    def __init__(self, nome, cpf):
        # Inicializa o cliente com nome e CPF
        self.cpf = cpf
        self.nome = nome

    def gravar_cliente(self):
        # Grava as infos do cliente no arquivo
        with open('Clientes.txt', 'a') as arq_cli:
            arq_cli.write(f" Nome: {self.nome}\n"
                          f" CPF: {self.cpf}\n"
                          f"|==================================|\n")

    @staticmethod
    def ler_arq_cli():
        # Da print no arquivo clientes
        with open('Clientes.txt', 'r') as f:
            print('\n|======| Leitura de cliente |======|')
            print(f.read())


class Conta(Cliente):
    def __init__(self, nome="", cpf="", n_conta="", saldo=0):
        # Inicializa a conta com informacoes do cliente, numero da conta e saldo
        super().__init__(nome, cpf)
        self.n_conta = n_conta
        self.saldo = saldo

    # Criando instancia do historico
    historico = Historico()

    def gravar_conta(self):
        # Carrega as contas que ja tao no arquivo
        contas = self.ler_contas()

        # Adiciona ou atualiza uma conta no dicionario
        contas[self.n_conta] = {
            'nome': self.nome,
            'cpf': self.cpf,
            'saldo': self.saldo
        }

        # Grava o dicionario atualizado no arquivo
        with open('Contas.json', 'w') as arq_contas:
            json.dump(contas, arq_contas, indent=2)

    @staticmethod
    def ler_contas():
        try:
            # Le as contas do arquivo e retorna como dicionario
            with open('Contas.json', 'r') as arq_contas:
                content = arq_contas.read()
                if not content:
                    return {}
                return json.loads(content)
        except FileNotFoundError:
            return {}
        except json.decoder.JSONDecodeError:
            print("Erro de decodificacao JSON. Verifique o conteudo do arquivo 'Contas.json'.")
            return {}

    @staticmethod
    def printar_arq_conta():
        # Printa o arquivo
        contas = Conta.ler_contas()
        if contas:
            print('|======| Lista das contas |======|')
            for n_conta, info_conta in contas.items():
                print(f"Numero da Conta: {n_conta}")
                print(f"Nome: {info_conta['nome']}")
                print(f"CPF: {info_conta['cpf']}")
                print(f"Saldo: {info_conta['saldo']}")
                print("-------------------------------")
        else:
            print("Nenhuma conta encontrada.")

    def depositar(self, valor):
        # Carrega contas existentes do arquivo
        contas = self.ler_contas()

        # Atualiza o saldo na conta
        self.saldo += valor

        # Atualiza o saldo no dicionario
        contas[self.n_conta]['saldo'] = self.saldo

        # Grava o dicionario atualizado no arquivo
        with open('Contas.json', 'w') as arq_contas:
            json.dump(contas, arq_contas, indent=2)

        # Adiciona a transacao ao historico
        transacao = f'Deposito de {valor} na conta numero {self.n_conta}. {datetime.datetime.today()}'
        self.historico.gravaHistorico(transacao)

    def sacar(self, valor):
        # Carregaas contas existentes do arquivo
        contas = self.ler_contas()

        if self.saldo < valor:
            return False
        else:
            # Atualiza o saldo da conta
            self.saldo -= valor

            # Atualiza o saldo no dicionario contas
            contas[self.n_conta]['saldo'] = self.saldo

            # Grava o dicionario atualizado no arquivo de contas
            with open('Contas.json', 'w') as arq_contas:
                json.dump(contas, arq_contas, indent=2)

            # Adiciona a transacao no historico
            transacao = f'Saque de {valor} da conta numero {self.n_conta}. {datetime.datetime.today()}'
            self.historico.gravaHistorico(transacao)
            return True

    def transferir(self, conta_destino, valor):
        # Carrega as contas existentes do arquivo
        contas = self.ler_contas()

        if self.saldo >= valor:
            # Atualiza o saldo na conta de destino - Que vai receber
            conta_destino.saldo += valor
            # Atualiza o saldo na conta de origem - Que deu o dinheiro
            self.saldo -= valor

            # Atualiza os saldos no dicionario contas
            contas[self.n_conta]['saldo'] = self.saldo
            contas[conta_destino.n_conta]['saldo'] = conta_destino.saldo

            # Grava o dicionario atualizado no arquivo de cotnas
            with open('Contas.json', 'w') as arq_contas:
                json.dump(contas, arq_contas, indent=2)

            print("Transferencia realizada!")

            transacao = f'Transferencia da conta {self.n_conta} no valor de {valor} para conta {conta_destino.n_conta}. {datetime.datetime.today()}'
            self.historico.gravaHistorico(transacao)
        else:
            print("Saldo insuficiente para realizar a transferencia.")

