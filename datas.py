class Data:
    def __init__(self, dia, mes, ano):
        self.dia = str(dia).zfill(2)
        self.mes = str(mes).zfill(2)
        self.ano = str(ano).zfill(4)

    def formatada(self) -> str:
        return f'{self.dia}/{self.mes}/{self.ano}'
