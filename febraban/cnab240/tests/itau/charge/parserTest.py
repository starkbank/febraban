from unittest.case import TestCase
from febraban.cnab240.itau.charge import SlipParser


shippingFile = \
"""
34100000         220018183000180                    07307 000000014446 4STARK BANK S A                                                        11712201822131100000004000000                                                      000            
34100011R0100030 2020018183000180                    07307 000000014446 4STARK BANK S A                                                                                                000000001712201817122018                                 
3410001300001P 0107307 000000014446 4109100000698        00000               0201201900000000189000000000099A18122018000000000000000000000000000000000000000000000000000000000000000000000000000000SBX-5204946345525248     0001590000000000000 
3410001300002Q 011000002349014118RAFAEL STARK                            AV PAULISTA 1159 586                    MORRO DOS INGLE01329000SAO PAULO      SP0000000000000000                                        000                            
34100015         0000340000160000000040325031600000000000000000000000000000000000000000000000000000000000000000000000000000                                                                                                                     
34199999         000001000036000000                                                                                                                                                                                                             
""".strip()



returnFile = \
"""
34100000         220018183000180                    07307 000000014446 4STARK BANK S A                BANCO ITAU S.A.                         217122018093712000110040                                                                          
34100011T0100030 2020018183000180                    07307 000000014446 4STARK BANK S A                                                                                                000001101712201817122018                                 
3410001300003T 0607307000000001444604109100000532        0               19122018000000000000111000028615SBX-5630441608445952     000000000000000000MATHEUS FERRAZ MEI                      000000000000000000000035000000000                   
3410001300004U 060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001712201800000000000000000000000000000000000                              00000000000000000000000       
3410001300005T 0607307000000001444604109100000540        0               19122018000000000001000000028615SBX-5694847495176192     000000000000000000MATHEUS FERRAZ MEI                      000000000000000000000035000000000                   
3410001300006U 060000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001712201800000000000000000000000000000000000                              00000000000000000000000       
34100015         00003400002100000000000166541000000000000000000000000000000000000000000000000000000000000000000000MT17/12S                                                                                                                     
34199999         000001000036                                                                                                                                                                                                                   
""".strip()


class ParserTest(TestCase):

    def testParseShippingFile(self):
        slip = SlipParser.parseText(shippingFile)[0]
        self.assertEqual(slip.identifier, "SBX-5204946345525248")
        self.assertEqual(slip.amountInCents, 1890000)
        self.assertEqual(slip.occurrences, ["01"])

    def testReturnShippingFile(self):
        slip = SlipParser.parseText(returnFile)[0]
        self.assertEqual(slip.identifier, "SBX-5630441608445952")
        self.assertEqual(slip.amountInCents, 111)
        # self.assertEqual(slip.occurrences, ["06"])
