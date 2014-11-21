import re

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

    def shouldSubmitMessage(self, message):
        if len(message) < self.minLength or len(message) > self.maxLength:
            return False
        if self.blockEmail(message):
            return False
        if self.blockNumber(message):
            return False



        return True
    # check if message is acceptable for submission

    def blockEmail(self, message):
        regex_pattern = r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)'
        return self.blockEmailAddress and re.search(regex_pattern, message)
    # check if message should be blocked because of an email address

    def blockNumber(self, message):

        return False

    # check if message should be blocked because of a phone number

    def isVulgar(self, message):
        return False
    # check if the message is classified as vulgar

    def isSexual(self, message):
        return False
    # check if the message is classified as sexual


if __name__ == '__main__':

    watchdog = ContentWatchdog(10, 140, True, True)
    messages = ['howdy fools, what\'s up with yall?',
                'yo yo yo test post #1642',
                'this has an email@address.com',
                'girl can I have yo numba? can I have it?',
                'ya try 911 fool',
                'its actually 348-555-4718',
                'Big Poppa\'s number be da following: (124) 555- 6843']

    for message in messages:
        result = 'Accepted: ' if watchdog.shouldSubmitMessage(message) else 'REJECTED: '
        print result + message

    pass

    #your code