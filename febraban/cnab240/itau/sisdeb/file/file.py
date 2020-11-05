from datetime import datetime
from .header import Header
from .trailer import Trailer
from ....libs.fileUtils import FileUtils


class File:

    def __init__(self):
        self.header = Header()
        self.lots = []
        self.trailer = Trailer()

    def addLot(self, lot):
        lot.setLotNumber(len(self.lots) + 1)
        self.lots.append(lot)

    def toString(self, currentDatetime=None):
        lotsToString = "\r\n".join([lot.toString() for lot in self.lots])
        self.header.setGeneratedFileDate(currentDatetime or datetime.now())
        self.trailer.setNumberOfLotsAndRegisters(
            num=len(self.lots),
            sum=2 + self._countRegistersInLots()
        )
        return "%s\r\n%s\r\n%s\r\n" % (
            self.header.content,
            lotsToString,
            self.trailer.content
        )

    def setSender(self, sender):
        self.header.setSender(sender)
        self.header.setSenderBank(sender.bank)
        self.trailer.setSenderBank(sender.bank)

    def setBankAgreementCode(self, code):
        self.header.setBankAgreementCode(code)

    def output(self, fileName, path="/../", content=None, currentDatetime=None):
        file = FileUtils.create(name=fileName, path=path)
        file.write(self.toString(currentDatetime or datetime.now()) if not content else content)
        file.close()

    def _countRegistersInLots(self):
        count = 0
        for lot in self.lots:
            count += lot.count
        return count
