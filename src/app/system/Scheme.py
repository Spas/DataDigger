__author__="spas"
__date__ ="$29.09.2011 11:16:43$"

class Scheme():
    def __init__(self):
        self._schemeElements = {}
        self._rootElements = {}

    def addElement(self, element):
        """
        @desc Add new element to scheme
        @param element: SchemeElement
        @return SchemeElement
        """

    def getElementByName(self, element_name):
        """
        @param element_name: string
        @return SchemeElement
        """

    def getRootElements(self):
        """
        @return dict of SchemeElement (keys are SchemeElement.name)
        """

    def getElements(self):
        """
        @return dict of SchemeElement (keys are SchemeElement.name)
        """

    def generateCode(self, language):
        """
        @desc Generate source code for scheme
        @param language: int
        @return string
        """

    def execute(self, language):
        """
        @desc Execute scheme source code
        @param language: int
        @return bool
        """

    