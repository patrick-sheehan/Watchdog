
class ContentWatchdog:
    def __init__(self, minLength, maxLength, blockPhoneNumbers, blockEmailAddress):
        self.minLength = minLength
        self.maxLength = maxLength
        self.blockPhoneNumbers = blockPhoneNumbers
        self.blockEmailAddress = blockEmailAddress
        pass

    # Adjust variables to preference
    # minLength = 10
    # maxLength = 140
    # blockPhoneNumbers = True
    # blockEmailAddress = True

    @staticmethod
    def shouldBeSubmitted(self, message):
        if len(message) < self.minLength or len(message) > self.maxLength:
            return False
        if self.blockEmail(message):
            return False
        if self.blockNumber(message):
            return False



        return True
    # check if message is acceptable for submission

    def blockEmail(self, message):
        return False
    # check if message should be blocked because of an email address

    def blockNumber(self, message):
        return False
    # check if message should be blocked because of a phone number

    def isVulgar(self, message):
        return False
    # check if the message is classified as vulgar

    def isSexual:
        return False
    # check if the message is classified as sexual


