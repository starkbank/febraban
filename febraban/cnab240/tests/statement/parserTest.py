from unittest.case import TestCase
from febraban.cnab240.statement import StatementParser

returnFile = \
"""
07700000         223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA         BANCO INTER S.A.                        21211202016361800001610100000                                                      000            
07700011E0440033 223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                                                 17082020000000000000732846CFBRL00016                                                              
0770001300001E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S1908202019082020000000000000082240D1127059PAGAMENTO DE TITULO      026135                                 
0770001300002E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2008202020082020000000000000264357D1127045PAGAMENTO DE CONVENIO    000000                                 
0770001300003E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2008202020082020000000000000433675D1127045PAGAMENTO DE CONVENIO    000000                                 
0770001300004E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2008202020082020000000000000084054D1127045PAGAMENTO DE CONVENIO    000000                                 
0770001300005E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2008202020082020000000000000200000C2067211RESGATE                  672827                                 
0770001300006E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000144000C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300007E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000600000C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300008E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000100000C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300009E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000131800C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300010E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000098000C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300011E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2108202021082020000000000000080000C2017193DEPOSITO BOLETO 24 HORAS 000000                                 
0770001300012E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2408202024082020000000000000300000D1207065TED ENVIADA              025012                                 
0770001300013E   223130935000198                    0000190000014054310 KMEE INFORMATICA LTDA                  00                    S2508202025082020000000000000076900C2097067TED RECEBIDA             671091                                 
07700015         223130935000198                    0000190000014054310                 00000000000000000000000000000000000000000000000000000025082020000000000000999220CF000015000000000001164326000000000001430700                            
07799999         000001000017000001                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
""".strip()


class ParserTest(TestCase):

    def testReturnStatementFile(self):
        statement = StatementParser.parseText(returnFile)

        debit = 0
        credit = 0

        for line in statement.lines:
            if line.debit_credit == 'D':
                debit += line.amountInCents
            elif line.debit_credit == 'C':
                credit += line.amountInCents

        self.assertEqual(statement.debit_sum_in_cents, debit)
        self.assertEqual(statement.credit_sum_in_cents, credit)
