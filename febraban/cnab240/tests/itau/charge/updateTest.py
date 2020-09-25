from unittest.case import TestCase
from febraban.cnab240.itau.charge import SegmentP, SegmentQ, SegmentR
from febraban.cnab240.user import User, UserBank, UserAddress
from febraban.cnab240.itau.charge import Slip, File
from datetime import datetime, timedelta

orignalDate = datetime(day=20, month=07, year=2019)
now = datetime.now()
expiration = now + timedelta(days=1)

bank = UserBank(
    bankId="341",
    branchCode="1234",
    accountNumber="1234567",
    accountVerifier="8"
)

address = UserAddress(
    streetLine1="AV PAULISTA 1000",
    city="SAO PAULO",
    stateCode="SP",
    zipCode="01310000"
)

payer = User(
    name="ARYA STARK",
    identifier="12345678901",
    address=UserAddress(
        streetLine1="AV PAULISTA 1234",
        district="BELA VISTA",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01348002"
    )
)

guarantor = User(
    name="SACADOR",
    identifier="09876543210",
    bank=UserBank(
        bankId="341",
        branchCode="7307",
        accountNumber="14446",
        accountVerifier="4",
        bankName="BANCO ITAU SA"
    ),
    address=UserAddress(
        streetLine1="AV PAULISTA 1000",
        streetLine2="CJ 601",
        city="SAO PAULO",
        stateCode="SP",
        zipCode="01310000"
    )
)


class UpdateTest(TestCase):

    def testSegmentPlengh(self):
        string = SegmentP().content
        self.assertEqual(len(string), 240)

    def testSegmentPdefaultValues(self):
        content = SegmentP().content
        self.assertEqual(content[3:7], "0001")
        self.assertEqual(content[7:8], "3")
        self.assertEqual(content[13:14], "P")
        self.assertEqual(content[15:17], "01")
        self.assertEqual(content[37:40], "109")
        self.assertEqual(content[106:108], "99")
        self.assertEqual(content[108:109], "A")

    def testSegmentPsets(self):
        segment = SegmentP()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setAmountInCents(22500)
        segment.setExpirationDate("14062019")
        segment.setIssueDate("12062019")
        segment.setBankIdentifier(identifier="99999", dac="7")
        segment.setIdentifier("VITAO")
        segment.setOverdueLimit(overdueLimit=59)
        print(segment.content)
        response = "3410001300001P 0101234 000001234567 8109000999997        00000               1406201900000000002250000000099A12062019000000000000000000000000000000000000000000000000000000000000000000000000000000VITAO                    0001590000000000000 "
        self.assertEquals(segment.content, response)

    def testSegmentQsets(self):
        segment = SegmentQ()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setPayer(payer)
        segment.setPayerAddress(address)
        segment.setGuarantor(guarantor)
        segment.setCancel()
        response = "3410001300001Q 021000012345678901ARYA STARK                              AV PAULISTA 1000                                       01310000SAO PAULO      SP1000009876543210SACADOR                                 000                            "
        self.assertEquals(segment.content, response)

    def testSegmentRsets(self):
        segment = SegmentR()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setCancel()
        segment.setFine(date="14062019", fine=2)  # Tests with fine
        response = "3410001300001R 02000000000000000000000000000000000000000000000000214062019000000000000002                                                                                                              0000000000000000 000000000000  0         "
        self.assertEqual(segment.content, response)

    def testUpdateAmount(self):
        # Update Amount Test
        file = File()
        file.setSender(guarantor)
        file.setIssueDate(now)
        slip = Slip()
        slip.setSender(guarantor)
        slip.setPayer(payer)
        slip.setExpirationDate(orignalDate)
        slip.setBankIdentifier(
            identifier="2613",
            branch=bank.branchCode,
            accountNumber=bank.accountNumber,
            wallet="109"
        )
        slip.setIdentifier("PRD-5701383420379136")
        slip.chargeUpate(amount=125)
        file.add(register=slip)

        responseP = "3410001300001P 3107307 000000014446 4109000026130        00000               0000000000000000000012500000099A16072019000000000000000000000000000000000000000000000000000000000000000000000000000000PRD-5701383420379136     0000000000000000000 "
        responseQ = "3410001300002Q 010000000000000000                                                                                               00000000                 0000000000000000                                        000                            "
        responseR = "3410001300003R 010000000000000000000000000000000000000000000000000                                                                                                                                     0000000000000000 000000000000  0         "

        print(file.toString())
        print("")
        print(responseP)

        self.assertIn(responseP, file.toString())
        self.assertIn(responseQ, file.toString())
        self.assertIn(responseR, file.toString())

    def testUpdatedueDate(self):
        # Update dueDate Test
        file = File()
        file.setSender(guarantor)
        file.setIssueDate(now)
        slip = Slip()
        slip.setSender(guarantor)
        slip.setAmountInCents("100")
        slip.setPayer(payer)
        slip.setIssueDate(now)
        slip.setExpirationDate(orignalDate)
        slip.setBankIdentifier(
            identifier="2643",
            branch=bank.branchCode,
            accountNumber=bank.accountNumber,
            wallet="109"
        )
        slip.setIdentifier("PRD-5207112409939968")
        slip.setFineAndInterest(datetime=expiration, fine="0", interest="0")
        slip.setOverdueLimit("3")
        slip.chargeUpate(dueDate=expiration)
        file.add(register=slip)
        responseP = "3410001300001P 0607307 000000014446 4109000026437        00000               1707201900000000000010000000099A16072019017072019000000000000000000000000000000000000000000000000000000000000000000000PRD-5207112409939968     0000000000000000000 "
        responseQ = "3410001300002Q 010000000000000000                                                                                               00000000                 0000000000000000                                        000                            "
        responseR = "3410001300003R 01000000000000000000000000000000000000000000000000017072019000000000000000                                                                                                              0000000000000000 000000000000  0         "
        print(file.toString())
        self.assertIn(responseP, file.toString())
        self.assertIn(responseQ, file.toString())
        self.assertIn(responseR, file.toString())
