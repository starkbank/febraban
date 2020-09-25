from datetime import datetime
from ....row import Row
from ....characterType import numeric, alphaNumeric


class HeaderLot:

    def __init__(self):
        self.content = "00000000 0000000 0000000000000000                    00000 000000000000 0                                                                                                              000000000000000000000000                                 "
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7, 4,      numeric, "1"),
            (  7,   8, 1,      numeric, "1"),
            (  8,   9, 1, alphaNumeric, "R"),
            (  9,  11, 2,      numeric, "01"),
            ( 13,  16, 3,      numeric, "030"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setGeneratedFileDate(self, dateAndTime):
        if dateAndTime is None:
            dateAndTime = datetime.now()

        structs = [
            (191, 199, 8, numeric, dateAndTime.strftime("%d%m%Y")),   # Data de gravacao
            (199, 207, 8, numeric, dateAndTime.strftime("%d%m%Y")),   # Data de credito
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"),
            (18,  33, 15,      numeric, user.identifier),
            (73, 103, 30, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (  0,   3,  3,      numeric, bank.bankId),
            ( 54,  58,  4,      numeric, bank.branchCode),
            ( 59,  71, 12,      numeric, bank.accountNumber),
            ( 72,  73,  1,      numeric, bank.accountVerifier)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)