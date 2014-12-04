#
#  PythonStuff.py
#  PyRu
#
#  Created by Bill Bumgarner on 11/24/07.
#  Copyright (c) 2007 __MyCompanyName__. All rights reserved.
#

try:
    from Foundation import *
except:
    print "handled foundation exception"

import objc

NSObject = objc.lookUpClass(u"NSObject")
class PythonStuff(NSObject):
    _arrayOfStrings = ["Apples", "Bananas", "Pigs", "Turtles"]
    
    def init(self):
        super(PythonStuff, self).init()
        rubyStuffClass = objc.lookUpClass(u"RubyStuff")
        rubyStuff = rubyStuffClass.new()
        rawStrings = rubyStuff.getStuff(["Apples", "Bananas", "Pigs", "Turtles"])
        self._arrayOfStrings = [{"name" : x} for x in rawStrings]
        return self
    
    def arrayOfNamedStrings(self):
        return self._arrayOfStrings
    arrayOfNamedStrings = objc.accessor(arrayOfNamedStrings)
