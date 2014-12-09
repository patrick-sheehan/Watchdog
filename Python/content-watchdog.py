import re

class ContentWatchdog:
    def __init__(self, minLength, maxLength, blockPhone, blockEmail, blockVulgar):
        self.minLength = minLength
        self.maxLength = maxLength
        self.blockPhone = blockPhone
        self.blockEmail = blockEmail
        self.blockVulgar = blockVulgar
        pass

    # Can adjust hard-coded variables instead of using init method
    # minLength = 10
    # maxLength = 140
    # blockPhone = True
    # blockEmail = True

    def should_submit_message(self, message):

        accepted = True

        if len(message) < self.minLength or len(message) > self.maxLength:
            print 'LENGTH REJECTION : ' + message
            accepted = False
        if self.should_block_for_email(message):
            print 'EMAIL REJECTION  : ' + message
            accepted = False
        if self.should_block_for_number(message):
            print 'PHONE REJECTION  : ' + message
            accepted = False
        if self.should_block_for_vulgar(message):
            print 'VULGAR REJECTION : ' + message
            accepted = False

        if accepted:
            print 'Accepted!        : ' + message
            return True

        return False
    # check if message is acceptable for submission

    def is_valid_length(self, message):
        if len(message) < self.minLength or len(message) > self.maxLength:
            return True

        return False
    #check if message is in the valid size range

    def should_block_for_number(self, message):
        if self.blockPhone:
            listOfNumbers = map(int, re.findall('\d+', message))
            numberString = ""
            for number in listOfNumbers:
                numberString += str(number)

            if len(numberString) == 10:
                return True

        return False
    # check if message should be blocked because of a phone number

    def should_block_for_email(self, message):
        if self.blockEmail:
            regex_pattern = r'([\w\-\.]+@(\w[\w\-]+\.)+[\w\-]+)'
            if re.search(regex_pattern, message) is not None:
                return True

        return False
    # check if message should be blocked because of an email address

    def should_block_for_vulgar(self, message):
        if self.blockVulgar:
            words_file = open("../Resources/bad_words.txt")
            bad_words = words_file.read().split('\n')

            for word in message.split(' '):
                if bad_words.__contains__(word.lower()):
                    return True

        return False
    # check if the message is classified as vulgar

    def should_block_for_sexual(self, message):
        return False
    # check if the message is classified as sexual

if __name__ == '__main__':

    watchdog = ContentWatchdog(10, 140, True, True, True)
    messages = ['howdy fools, what\'s up with yall?',
                'This has some shit and poop words in it',
                'yo yo yo test post #1642',
                'this has an email@address.com',
                'girl can I have yo numba? can I have it?',
                'ya try 911 fool',
                'its actually 348-555-4718',
                'Big Poppa\'s number be da following: (124) 555- 6843',
                'Can I get away with my roommates phone number? as245j - 586 whoops 5453']

    for message in messages:
        result = watchdog.should_submit_message(message)

    pass