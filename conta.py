class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saca(self, valor):
        if self.pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite!")

    def extrato(self) -> str:
        return self.__saldo

    def transfere(self, valor, destino):
        if self.__saldo >= valor:
            self.__saldo -= valor
            destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


if __name__ == '__main__':
    conta1 = Conta('123-4', 'Jose', 0.0, 1000.0)
    conta1.deposita(500.0)
    conta1.saca(100.0)
    extrato = conta1.extrato()
    print('O extrato da conta é: R$ {}.2f'.format(extrato))
