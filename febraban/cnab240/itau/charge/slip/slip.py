from ....libs.dac import DAC
from .segmentP import SegmentP
from .segmentQ import SegmentQ
from .segmentR import SegmentR


class Slip:

    def __init__(self):
        self.segmentP = SegmentP()
        self.segmentQ = SegmentQ()
        self.segmentR = SegmentR()

    def toString(self):
        return "%s\r\n%s\r\n%s" % (self.segmentP.content, self.segmentQ.content, self.segmentR.content)

    def amountInCents(self):
        return self.segmentP.amountInCents()

    def setPositionInLot(self, index):
        self.segmentP.setPositionInLot(index)
        self.segmentQ.setPositionInLot(index+1)
        self.segmentR.setPositionInLot(index+2)

    def setSender(self, user):
        self.segmentP.setSenderBank(user.bank)
        self.segmentQ.setSenderBank(user.bank)
        self.segmentR.setSenderBank(user.bank)

    def setPayer(self, user):
        self.segmentQ.setPayer(user)
        self.segmentQ.setPayerAddress(user.address)

    def setGuarantor(self, user):
        self.segmentQ.setGuarantor(user)

    def setAmountInCents(self, value):
        self.segmentP.setAmountInCents(value)

    def setExpirationDate(self, datetime):
        self.segmentP.setExpirationDate(datetime.strftime("%d%m%Y"))

    def setIssueDate(self, datetime):
        self.segmentP.setIssueDate(datetime.strftime("%d%m%Y"))

    def setBankIdentifier(self, identifier, branch, accountNumber, wallet):
        dac = DAC.calculate(
            branch="{:0>4}".format(branch)[:4],
            accountNumber=accountNumber,
            wallet="{:0>3}".format(wallet)[:3],
            bankNumber="{:0>8}".format(identifier)[:8]
        )
        self.segmentP.setBankIdentifier(identifier, dac)

    def setIdentifier(self, identifier):
        self.segmentP.setIdentifier(identifier)

    def setFineAndInterest(self, datetime, fine, interest):
        self.segmentP.setInterest(datetime.strftime("%d%m%Y"), interest)
        self.segmentR.setFine(datetime.strftime("%d%m%Y"), fine)

    def setOverdueLimit(self, overdueLimit):
        self.segmentP.setOverdueLimit(overdueLimit)

    def setCancel(self):
        self.segmentP.setCancel()
        self.segmentQ.setCancel()
        self.segmentR.setCancel()

    def chargeUpate(self, amount=None, fine=None, dueDate=None, fineDate=None):
        if amount:
            self.segmentP.chargeUpdateAmount(amount)
        if fine:
            self.segmentP.chargeUpdateFine()
            self.segmentQ.chargeUpdateFine()
            self.segmentR.setFine(date=fineDate.strftime("%d%m%Y"), fine=fine)
        if dueDate:
            self.segmentP.chargeUpdateDueDate(dueDate.strftime("%d%m%Y"))

