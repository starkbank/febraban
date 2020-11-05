from febraban.cnab240.itau.sisdeb import PaymentParser


file = open("output-debit.RET", "r")

responses = PaymentParser.parseFile(file)

for response in responses:
    print "-------------------------------------------------------------------"
    print response.identifier
    print response.authentication
    print response.status()
    print response.amountInCents
    print response.type
    print response.contentText()
