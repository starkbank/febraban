from febraban.cnab240.statement import StatementParser

file = open("output.RET", "r")

statement = StatementParser.parseFile(file)

debit = 0
credit = 0

print(statement.bank_code)
print(statement.branch_number, '-', statement.branch_code)
print(statement.account_number, '-', statement.account_code)

for line in statement.lines:
    print(line.occurrence)
    print(line.cpmf)
    print(line.date_account)
    print(line.date_move)
    print(line.amountInCents)
    print(line.debit_credit)
    print(line.amountInCents)
    print(line.occurrence)
    print(line.bank_history_code)
    print(line.bank_history_description)
    print(line.bank_history_description)
    print(line.occurrenceText())
    print(line.contentText())

    if line.debit_credit == 'D':
        debit += line.amountInCents
    elif line.debit_credit == 'C':
        credit += line.amountInCents

if not statement.debit_sum_in_cents == debit:
    raise Exception

if not statement.credit_sum_in_cents == credit:
    raise Exception
