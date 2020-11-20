class User:

    def __init__(self, name, identifier, bank=None, address=None, email=None,
                 phone=None, personType=None):
        self.name = name
        self.identifier = identifier
        self.bank = bank
        self.address = address
        self.email = email
        self.phone = phone
        self.personType = personType


class UserBank:

    def __init__(self, bankId, branchCode, accountNumber, accountVerifier, bankName=""):
        self.bankId = bankId
        self.bankName = bankName
        self.accountNumber = accountNumber
        self.branchCode = branchCode
        self.accountVerifier = accountVerifier


class UserAddress:

    def __init__(self, streetLine1, city, stateCode, zipCode, district="",
                 streetLine2="", streetNumber=None):
        self.streetLine1 = streetLine1
        self.streetLine2 = streetLine2
        self.district = district
        self.city = city
        self.stateCode = stateCode
        self.zipCode = zipCode
        self.streetNumber = streetNumber
