# coding: utf-8

from ....characterType import numeric, alphaNumeric
from ....row import Row


class SegmentA:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def amountInCents(self):
        return int(self.content[119:134])

    def defaultValues(self):
        structs = [
            (  3,   7,  4,      numeric, "1"),
            (  7,   8,  1,      numeric, "3"),
            ( 13,  14,  1, alphaNumeric, "A"),
            ( 14,  20,  6,      numeric, "0"),
            (101, 104,  3, alphaNumeric, "REA"),
            (104, 119, 15,      numeric, "0"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (0,   3,  3, numeric, user.bank.bankId),              # Código do # banco debitado
            (216, 230, 14, numeric, user.identifier)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiver(self, user):
        structs = [
            ( 43,  73, 30,  alphaNumeric, user.name),        # Nome FAvorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setReceiverBank(self, bank):
        structs = [
            (20, 23,  3,  numeric, bank.bankId),             # Código do banco do Favorecido
            (23, 28,  5,  numeric, bank.branchCode),         # Agencia Favorecido
            (29, 41, 12,  numeric, bank.accountNumber),      # Conta Favorecido
            (42, 43,  1,  numeric, bank.accountVerifier),    # DAC FAvorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setAmountInCents(self, amount):
        structs = [
            (119, 134, 15, numeric, amount)                  # Valor ao Favorecido
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index),                       # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setLot(self, lot):
        structs = [
            (3,  7, 4, numeric, lot),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setScheduleDate(self, date):
        structs = [
            (93, 101, 8, numeric, date)                      # Data para transferencia
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setIdentifier(self, identifier):
        structs = [
            (73, 93, 20, alphaNumeric, identifier)           # Id da empresa na transação
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFee(self, identifier):
        structs = [
            (177, 179, 2, numeric, identifier)           # Mora 00 = isento
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setFeePrice(self, price):
        structs = [
            (179, 196, 17, numeric, price)           # valor da mora
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
