class usuario:
    def __init__(self, nome, sobrenome, sexo, cpf):

        self.nome = nome
        self.sobrenome = sobrenome
        self.sexo = sexo
        self.cpf = cpf 


class historico:
    def __init__(self, data_abertura, transsacoes, datetime):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []
    
    def imprime(self):
        print("data de abertura: {}".format(self.data_abertura))
        print("transacoes: ")
        for t in self.transacoes:
            print("-", t)


class conta:
    def __init__(self, numero, usuario, saldo, historico, limite=100):

        self.numero = numero
        self.usuario = usuario
        self.saldo = saldo
        self.limite = limite
        self.historico = historico()

    def depositar(self, valor):

        self.saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))


    def saca(self, valor):

        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):

        print("numero: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True
            


