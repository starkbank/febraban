# coding: utf-8

from ....row import Row
from ....characterType import numeric, alphaNumeric


class HeaderLot:

    def __init__(self):
        self.content = " " * 240
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (  3,   7, 4,      numeric, "1"),
            (  7,   8, 1,      numeric, "1"),
            (  8,   9, 1, alphaNumeric, "D"),
            ( 13,  16, 3,      numeric, "030"),
            ( 58,  65, 7,      numeric, "0000000"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSender(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"),
            (18,  32, 14,      numeric, user.identifier),
            (72, 102, 30, alphaNumeric, user.name)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            ( 0,   3,  3, numeric, bank.bankId),
            (52,  57,  5, numeric, bank.branchCode),
            (65,  70,  5, numeric, bank.accountNumber),
            (71,  72,  1, numeric, bank.accountVerifier),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderAddress(self, address):
        structs = [
            (142, 192, 50, alphaNumeric, "%s %s %s" % (address.streetLine1, address.streetLine2, address.district)),
            (192, 212, 20, alphaNumeric, address.city),
            (212, 220,  8,      numeric, address.zipCode),
            (220, 222,  2, alphaNumeric, address.stateCode),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (3, 7, 4, numeric, index)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setInfo(self, kind, method):
        structs = [
            ( 9, 11, 2, numeric, kind),
            (11, 13, 2, numeric, method)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setBankAgreementCode(self, code):
        structs = [
            (32, 45, 13, alphaNumeric, code),
            ]
        self.content = Row.setStructs(structs=structs, content=self.content)