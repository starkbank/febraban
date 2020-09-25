from datetime import datetime
from ....row import Row
from ....characterType import numeric, alphaNumeric


class Header:

    def __init__(self):
        self.content = "00000000         000000000000000                    00000 000000000000 0                                                                      00000000000000000000000000000                                                      000            "
        self.defaultValues()

    def defaultValues(self):
        structs = [
            (142, 143, 1, numeric, "1"),    # 1 = Remessa, 2 = Retorno
            (163, 166, 3, numeric, "040"),  # Layout do arquivo
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setGeneratedFileDate(self, dateAndTime):
        if dateAndTime is None:
            dateAndTime = datetime.now()

        structs = [
            (143, 151, 8, numeric, dateAndTime.strftime("%d%m%Y")),   # Dia que o arquivo foi gerado
            (151, 157, 6, numeric, dateAndTime.strftime("%H%M%S")),   # Horario que o arquivo foi gerado
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
            (  0,   3,  3,      numeric, bank.bankId),
            ( 52,  57,  5,      numeric, bank.branchCode),
            ( 58,  70, 12,      numeric, bank.accountNumber),
            ( 71,  72,  1,      numeric, bank.accountVerifier),
            (102, 132, 30, alphaNumeric, bank.bankName)
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)
