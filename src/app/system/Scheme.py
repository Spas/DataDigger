__author__="spas"
__date__ ="$29.09.2011 11:16:43$"

class Scheme():
    def __init__(self):
        self._schemeElements = {}
        self._rootElements = {}

    """
    @desc Add new element to scheme
    @param element: SchemeElement
    @return SchemeElement
    """
    def addElement(self, element):
        self._elements[element.getName()] = element

    """
    @param element_name: string
    @return SchemeElement
    """
    def getElementByName(self, element_name):
        if self._elements.has_key(element_name):
            return self._elements[element_name]
        else:
            return None

    """
    @return dict of SchemeElement (keys are SchemeElement.name)
    """
    def getRootElements(self):
       pass

    """
    @return dict of SchemeElement (keys are SchemeElement.name)
    """
    def getElements(self):
        return self._elements

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

    