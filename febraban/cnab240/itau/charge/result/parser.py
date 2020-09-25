from .occurrences import occurrences
from .errors import errors03, errors17, errors15, errors16, errors18


class SlipResponseStatus:

    registered = "registered"
    paid = "paid"
    canceled = "canceled"
    updated = "updated"
    overdue = "overdue"
    failed = "failed"
    unknown = "unknown"


class SlipResponse:

    def __init__(self, identifier=None, occurrence=None, content=None, amountInCents=None, fine=None, discount=None, errors=None):
        self.identifier = identifier
        self.occurrence = occurrence
        self.amountInCents = amountInCents
        self.fine = fine
        self.discount = discount
        self.content = content or []
        self.errors = errors or []

    def occurrenceText(self):
        return occurrences[self.occurrence]

    def status(self):
        if self.occurrence == "02":
            return SlipResponseStatus.registered
        if self.occurrence in ["03", "15", "16", "17", "18"]:
            return SlipResponseStatus.failed
        if self.occurrence in ["06", "08"]:
            return SlipResponseStatus.paid
        if self.occurrence == "09":
            return SlipResponseStatus.canceled
        if self.occurrence in ["04", "14"]:
            return SlipResponseStatus.updated
        return SlipResponseStatus.unknown

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)

    def failureErrors(self):
        errorDict = {
            "03": errors03,
            "15": errors15,
            "16": errors16,
            "17": errors17,
            "18": errors18,
        }.get(self.occurrence) or {}

        return [errorDict[errorCode] for errorCode in self.errors if errorCode in errorDict.keys()]

    def amountPaid(self):
        return self.amountInCents + self.fine - self.discount


class SlipParser:

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        return cls.parseLines(lines)

    @classmethod
    def parseText(cls, text):
        lines = text.splitlines()[:-1]
        return cls.parseLines(lines)

    @classmethod
    def parseLines(cls, lines):
        result = []
        for line in lines:
            if line[7] == "3" and line[13] == "T":
                currentResponse = SlipResponse()
                currentResponse.content.append(line)
                currentResponse.amountInCents = int(line[81:96])
                currentResponse.occurrence = line[15:17]
                currentResponse.identifier = line[105:130].strip()
                currentResponse.errors = [line[213 + i:215 + i] for i in range(0, 8, 2) if line[i:i + 2] != "  "]
            elif line[7] == "3" and line[13] == "U":
                currentResponse.content.append(line)
                currentResponse.fine = int(line[17:32])
                currentResponse.discount = int(line[32:47])
                result.append(currentResponse)
            elif line[7] == "3" and line[13] == "P":
                currentResponse = SlipResponse()
                currentResponse.content.append(line)
                currentResponse.amountInCents = int(line[85:100])
                currentResponse.occurrences = [line[15:17]]
                currentResponse.identifier = line[195:220].strip()
            elif line[7] == "3" and line[13] == "Q":
                currentResponse.content.append(line)
                result.append(currentResponse)
        return result
