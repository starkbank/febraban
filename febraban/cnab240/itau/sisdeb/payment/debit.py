from .segmentA import SegmentA


class Debit:

    def __init__(self):
        self.segmentA = SegmentA()

    def toString(self):
        return self.segmentA.content

    def amountInCents(self):
        return self.segmentA.amountInCents()

    def setSender(self, user):
        self.segmentA.setSender(user)

    def setReceiver(self, user):
        self.segmentA.setReceiver(user)
        self.segmentA.setReceiverBank(user.bank)

    def setAmountInCents(self, value):
        self.segmentA.setAmountInCents(value)

    def setPositionInLot(self, index):
        self.segmentA.setPositionInLot(index)

    def setLot(self, lot):
        self.segmentA.setLot(lot)

    def setScheduleDate(self, date):
        self.segmentA.setScheduleDate(date)

    def setIdentifier(self, identifier):
        self.segmentA.setIdentifier(identifier)

    def setFee(self, identifier):
        self.segmentA.setFee(identifier)

    def setFeePrice(self, price):
        self.segmentA.setFeePrice(price)
