from .occurrences import debit_occurrences, credit_occurrences


class Statement:

    def __init__(
            self, content=None, bank_code=None, branch_number=None, branch_code=None,
            account_number=None, account_code=None, start_date=None,
            start_amount_in_cents=None, start_debit_credit=None, stop_date=None,
            stop_amount_in_cents=None, stop_debit_credit=None, line_quantity=None,
            debit_sum_in_cents=None, credit_sum_in_cents=None, currency=None):
        self.content = content or []
        self.bank_code = bank_code
        self.branch_number = branch_number
        self.branch_code = branch_code
        self.account_number = account_number
        self.account_code = account_code
        self.start_date = start_date
        self.start_amount_in_cents = start_amount_in_cents
        self.start_debit_credit = start_debit_credit
        self.stop_date = stop_date
        self.stop_amount_in_cents = stop_amount_in_cents
        self.stop_debit_credit = stop_debit_credit
        self.line_quantity = line_quantity
        self.debit_sum_in_cents = debit_sum_in_cents
        self.credit_sum_in_cents = credit_sum_in_cents
        self.currency = currency
        self.amount = 0
        self.lines = []


class StatementLine:

    def __init__(self, content=None, occurrence=None, cpmf=None, date_account=None,
                 date_move=None, amountInCents=None, debit_credit=None,
                 bank_history_code=None, bank_history_description=None,
                 document_number=None, amount=None):
        self.content = content or []
        self.cpmf = cpmf
        self.date_account = date_account
        self.date_move = date_move
        self.amountInCents = amountInCents
        self.debit_credit = debit_credit
        self.occurrence = occurrence
        self.bank_history_code = bank_history_code
        self.bank_history_description = bank_history_description
        self.document_number = document_number
        self.amount = amount

    def occurrenceText(self):
        if self.occurrence and self.debit_credit == 'C':
            return credit_occurrences[self.occurrence]
        elif self.occurrence and self.debit_credit == 'D':
            return debit_occurrences[self.occurrence]

    def contentText(self, breakLine="\n"):
        return breakLine.join(self.content)


class StatementParser:

    def __init__(self, lines):
        self._lines = lines
        self.statement = None

    @classmethod
    def parseFile(cls, file):
        lines = file.readlines()
        statement = StatementParser(lines)
        return statement.parseLines()

    @classmethod
    def parseText(cls, text):
        lines = text.splitlines()[:-1]
        statement = StatementParser(lines)
        return statement.parseLines()

    def _prepare_statement_header(self, line):
        self.statement = Statement(
            content=[line],
            bank_code=line[0:3],
            branch_number=line[52:57],
            branch_code=line[57:58],
            account_number=line[58:70],
            account_code=line[57:58],
            start_date=line[142:150],
            start_amount_in_cents=int(line[150:168]),
            start_debit_credit=line[168:169],
            currency=line[170:173]
        )

    def _prepare_statement_footer(self, line):
        self.statement.content.append(line)
        self.statement.stop_date = line[142:150]
        self.statement.stop_amount_in_cents = int(line[150:168])
        self.statement.stop_debit_credit = line[168:169]
        self.statement.line_quantity = int(line[170:176])
        self.statement.debit_sum_in_cents = int(line[176:194])
        self.statement.credit_sum_in_cents = int(line[194:212])

    def _prepare_statement_line(self, line):
        statement_line = StatementLine()
        statement_line.content.append(line)
        statement_line.occurrence = line[15:17]
        statement_line.cpmf = line[133:134]
        statement_line.date_account = line[134:142]
        statement_line.date_move = line[142:150]
        statement_line.amountInCents = int(line[150:168])
        statement_line.debit_credit = line[168:169]
        statement_line.occurrence = line[169:172]
        statement_line.bank_history_code = line[172:176]
        statement_line.bank_history_description = line[176:201]
        statement_line.document_number = line[201:240]

        if statement_line.debit_credit == 'C':
            statement_line.amount = statement_line.amountInCents / 100
        elif statement_line.debit_credit == 'D':
            statement_line.amount = - statement_line.amountInCents / 100
        self.statement.amount += statement_line.amount
        self.statement.lines.append(statement_line)

    def parseLines(self):
        for line in self._lines:

            if line[7] in ["0", "9"]:
                continue
            if line[7] == "1" and line[8] == "E":
                if not self.statement:
                    self._prepare_statement_header(line)

            if line[7] == "5":
                self._prepare_statement_footer(line)

            if line[7] == "3" and line[13] == "E":
                self._prepare_statement_line(line)

        return self.statement
