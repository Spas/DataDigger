__author__="spas"
__date__ ="$29.09.2011 11:16:48$"

class SchemeElement():
    def __init__(self):
        self._id = ''
        self._name = ''
        self._description = ''
        self._module = null
        self._realization = null
        self._nextElements = {}
        self._prevElements = {}
        self._userParameters = null
        self._inputParameters = null
        self._outputParameters = null

    """
    @param name: string
    @return string
    """
    def setName(self, name):
        self._name = name
        return name

    """
    @return string
    """
    def getName(self):
        return self._name

    """
    @param description: string
    @return string
    """
    def setDescription(self, description):
        self._description = description

    """
    @return string
    """
    def getDescription(self):
        return self._description

    """
    @param module: app.system.Module
    @return app.system.Module
    """
    def setModule(self, module):
        self._module = module

    """
    @return app.system.Module
    """
    def getModule(self):
        return self._module

    """
    @param realization: app.system.code.realizations.ModuleRealization
    @return app.system.code.realizations.ModuleRealization
    """
    def setRealization(self, realization):
        self._realization = realization

    """
    @return app.system.code.realizations.ModuleRealization
    """
    def getRealization(self):
        return self._realization

    """
    @desc Add new element to _nextElements
    @param scheme_element: SchemeElement
    @return SchemeElement
    """
    def addNextSchemeElement(self, scheme_element):
        self._nextElements[scheme_element.getName()] = scheme_element

    """
    @desc Return dictionary of next scheme elements
    @return dict of SchemeElement
    """
    def getNextSchemeElements(self):
        return self._nextElements

    def deleteNextSchemeElement(self, scheme_element_name):
        """
        @desc Delete scheme_element with id as scheme_element_id
              from _nextElements dictionary (just remove elements connection,
              doesn`t delete element from scheme)
        @param scheme_element_id: string
        @return SchemeElement
        """

    def addPreviousSchemeElement(self, scheme_element):
        """
        @desc Add new element to _prevElements
        @param scheme_element: SchemeElement
        @return SchemeElement
        """

    def getPreviousSchemeElements(self):
        """
        @desc Return dictionary of previous scheme elements
        @return dict of SchemeElement
        """

    def deletePreviousSchemeElementById(self):
        """
        @desc Delete scheme_element with id as scheme_element_id
              from _prevElements dictionary (just remove elements connection,
              doesn`t delete element from scheme)
        @param scheme_element_id: string
        @return SchemeElement
        """

    def initParameters(self):
        """
        @desc Load user, input and output parameters lists from element`s
              module. Return false if module isn`t defined.
        @return bool
        """

    def getUserParametersList(self):
        """
        @desc Return user-defined-parameters list
        @return ParametersList
        """

    def getInputParametersList(self):
        """
        @desc Return input parameters list
        @return ParametersList
        """

    def getOutputParametersList(self):
        """
        @desc Return output parameters list
        @return ParametersList
        """

    def generateCode(self, language):
        """
        @desc Generate source code for element`s module realization
        @param language: int
        @return string
        """