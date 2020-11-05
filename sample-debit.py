
# coding: utf-8

from febraban.cnab240.itau.sisdeb import Debit, File
from febraban.cnab240.itau.sisdeb.file.lot import Lot
from febraban.cnab240.user import User, UserAddress, UserBank


sender = User(
    name="YOUR COMPANY NAME HERE",
    identifier="12345678901234",
    bank=UserBank(
        bankId="341",
        branchCode="4321",
        accountNumber="12345678",
        accountVerifier="9"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)

receiver1 = User(
    name="RECEIVER NAME HERE",
    identifier="01234567890",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="12345",
        accountVerifier="9"
    )
)

receiver2 = User(
    name="RECEIVER NAME HERE",
    identifier="01234567890",
    bank=UserBank(
        bankId="341",
        branchCode="1234",
        accountNumber="12345",
        accountVerifier="9"
    )
)

receivers = [receiver1, receiver2]

file = File()
file.setSender(sender)
file.setBankAgreementCode('CONV56789ENIO')

lot = Lot()

lot.setSender(sender)
lot.setBankAgreementCode('CONV56789ENIO')
lot.setHeaderLotType(
    kind="05",  #Tipo de serviço
    method="50" #FORMALANCTO
)

for receiver in receivers:
    payment = Debit()
    payment.setSender(sender)
    payment.setReceiver(receiver)
    payment.setAmountInCents("10000")
    payment.setFee('00')
    payment.setFeePrice("00000000000000000")
    payment.setScheduleDate("06052020")
    payment.setIdentifier("ID1234567890345")
    lot.add(register=payment)

file.addLot(lot)
file.output(fileName="output-debit.REM", path="/../../")

