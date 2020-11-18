

class DAC:

    @classmethod
    def calculate(cls, branch, accountNumber, wallet, bankNumber):
        x1 = branch + accountNumber + wallet + bankNumber
        x2 = "12" * int(len(x1) / 2) + ("1" if len(x1) % 2 == 1 else "")
        out = [int(a) * int(b) for (a, b) in zip(x1, x2)]
        s = sum(map(lambda x: int(x/10 + x % 10), out))
        return (10 - s % 10) % 10

    @classmethod
    def calculateTaxDac(cls, productId, segmentId, currency, amount, company, freeField):
        x1 = productId + segmentId + currency + amount + company + freeField
        x2 = "12" * int(len(x1) / 2) + ("1" if len(x1) % 2 == 1 else "")
        out = [int(a) * int(b) for (a, b) in zip(x1, x2)]
        s = sum(map(lambda x: int(x/10 + x % 10), out))
        return (10 - s % 10) % 10
