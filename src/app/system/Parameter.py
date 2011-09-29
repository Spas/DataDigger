__author__="spas"
__date__ ="$29.09.2011 11:17:41$"

class Parameter():
    def __init__(self, name, type, value = null):
        self._name = name
        self._type = type
        self._value = value

    def setName(self, name):
        """
        @param name: string
        @return string
        """

    def getName(self):
        """
        @return string
        """

    def setType(self, type):
        """
        @param type: string
        @return string
        """

    def getType(self):
        """
        @return string
        """

    def setValue(self, value):
        """
        @param value: object
        @return object
        """

    def getValue(self):
        """
        @return object
        """