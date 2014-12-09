import re

class ContentWatchdog:
    def __init__(self, minLength, maxLength, blockPhoneNumbers, blockEmailAddress):
        self.minLength = minLength
        self.maxLength = maxLength
        self.blockPhoneNumbers = blockPhoneNumbers
        self.blockEmailAddress = blockEmailAddress
        pass

    # Adjust hard coded variables instead of using init method
    # minLength = 10
    # maxLength = 140
    # blockPhoneNumbers = True
    # blockEmailAddress = True
    
    def new(self):
        self = super(ContentWatchdog, self).new()
        print u"new PythonStuff created" #for debugging
        if self is None:
            return None
        else:
            self.__init__()

        return self

    def pyTestMethod_(self, message):
        print 'The passed type is ' + str(type(message))
    

    def shouldSubmitMessage(self, message):
        if len(message) < self.minLength or len(message) > self.maxLength:
            print 'LENGTH REJECTION : ' + message
            return False
        if self.blockEmail(message):
            print 'EMAIL REJECTION  : ' + message
            return False
        if self.blockNumber(message):
            print 'PHONE REJECTION  : ' + message
            return False



        print 'Accepted!        : ' + message
        return True
    # check if message is acceptable for submission

    def shouldBlockForEmail(self, message):
        regex_pattern = r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)'
        if self.blockEmailAddress:
            if re.search(regex_pattern, message) is not None:
                return True

        return False
    # check if message should be blocked because of an email address

    def shouldBlockForNumber(self, message):
        listOfNumbers = map(int, re.findall('\d+', message))
        numberString = ""
        for number in listOfNumbers:
            numberString += str(number)

        if len(numberString) == 10:
            return True
        return False

    # check if message should be blocked because of a phone number

    def shouldBlockForVulgar(self, message):
        return False
    # check if the message is classified as vulgar

    def shouldBlockForSexual(self, message):
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
                'Big Poppa\'s number be da following: (124) 555- 6843',
                'Can I get away with my roommates phone number? as245j - 586 whoops 5453']

    for message in messages:
        result = watchdog.shouldSubmitMessage(message)

    pass

    #your code