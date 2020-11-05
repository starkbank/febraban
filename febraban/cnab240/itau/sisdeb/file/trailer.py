# coding: utf-8

from ....row import Row
from ....characterType import numeric


class Trailer:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,  8, 5, numeric, "99999"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setNumberOfLotsAndRegisters(self, sum, num):
        structs = [
            (17, 23, 6, numeric, num),
            (23, 29, 6, numeric, sum),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0,   3,  3, numeric, bank.bankId),              # Código do banco debitado
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
