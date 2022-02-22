class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def extrato(self) -> str:
        return self.saldo


if __name__ == '__main__':
    conta1 = Conta('123-4', 'Jose', 0.0, 1000.0)
    conta1.deposita(500.0)
    conta1.saca(100.0)
    extrato = conta1.extrato()
    print('O extrato da conta é: R$ {}.2f'.format(extrato))
