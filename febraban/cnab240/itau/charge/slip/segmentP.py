# coding: utf-8

from ....row import Row
from ....characterType import numeric, alphaNumeric


class SegmentP:

    def __init__(self):
        self.content = "0000000000000  0000000 000000000000 0000000000000        00000               0000000000000000000000000000000A00000000000000000000000000000000000000000000000000000000000000000000000000000000000000                         0000000000000000000 "
        self.defaultValues()

    def amountInCents(self):
        return int(self.content[85:100])

    def defaultValues(self):
        structs = [
            (  3,   7, 4,      numeric, "1"),
            (  7,   8, 1,      numeric, "3"),
            ( 13,  14, 1, alphaNumeric, "P"),
            ( 15,  17, 2,      numeric, "01"),
            ( 37,  40, 3,      numeric, "109"),               # Numero da Carteira de Cobranca
            (106, 108, 2,      numeric, "99"),                # Especie do Titulo: 99 = Real
            (108, 109, 1, alphaNumeric, "A"),                 # Aceite: A = Sim, N = Nao
            (223, 224, 1,      numeric, "1"),                 # 0 - Não baixe boletos, 1 - Baixe boletos após x dias do vencimento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setCancel(self):
        structs = [
            (15, 17, 2, numeric, "02"),                       # Indica Baixa do boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (  0,   3,  3,      numeric, bank.bankId),
            ( 18,  22,  4,      numeric, bank.branchCode),
            ( 23,  35, 12,      numeric, bank.accountNumber),
            ( 36,  37,  1,      numeric, bank.accountVerifier)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index)                        # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankIdentifier(self, identifier, dac):
        structs = [
            (40, 48, 8, numeric, identifier),                # Numero dado pelo Banco
            (48, 49, 1, numeric, dac)                        # Verificador do numero dado pelo Banco
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (85, 100, 15, numeric, amount),                  # Valor do Boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setExpirationDate(self, date):
        structs = [
            (77, 85, 8, numeric, date),                      # Data de vencimento do boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIssueDate(self, date):
        structs = [
            (109, 117, 8, numeric, date),                    # Data de emissao do boleto
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (195, 220, 25, alphaNumeric, identifier)          # Id da empresa na transação
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInterest(self, date, interest):
        structs = [
            (118, 126,  8, numeric, date),               # Data do juros mora
            (126, 141, 15, numeric, interest)            # Valor de mora por dia de atraso
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setOverdueLimit(self, overdueLimit):
        structs = [
            (224, 226, 2, numeric, overdueLimit),  # Quantidade de dias após o vencimento para baixa automática
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNullValues(self):
        structs = [
            (109, 117, 8, numeric, "0"),                # Data de emissao do boleto nula
            (77, 85, 8, numeric, "0"),                  # Data de vencimento do boleto nula
            (223, 224, 1, numeric, "0"),
            (224, 226, 2, numeric, "0"),                # Quantidade de dias após o vencimento nulo
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setOccurrence(self, occurence):
        structs = [
            (15, 17, 2, numeric, occurence)

        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def chargeUpdateDueDate(self, dueDate):
        self.setNullValues()
        structs = [
            (15, 17, 2, numeric, "06"),                 # Indica alteracao
            (77, 85, 8, numeric, dueDate),              # Alteracao vencimento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
