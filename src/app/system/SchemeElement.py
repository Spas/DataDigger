__author__="spas"
__date__ ="$29.09.2011 11:16:48$"

from copy import copy

class SchemeElement():
    def __init__(self):
        self._id = ''
        self._name = ''
        self._description = ''

        self._module = None
        self._realization = None

        self._next_elements = {}
        self._prev_elements = {}

        self._input_parameters = None
        self._user_parameters = None
        self._output_parameters = None

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
        return description

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
        return module

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
        return realization

    """
    @return app.system.code.realizations.ModuleRealization
    """
    def getRealization(self):
        return self._realization

    """
    @desc Add new element to _next_elements
    @param scheme_element: SchemeElement
    @return SchemeElement
    """
    def addNextSchemeElement(self, scheme_element):
        self._next_elements[scheme_element.getId()] = scheme_element
        return scheme_element

    """
    @desc Return dictionary of next scheme elements
    @return dict of SchemeElement
    """
    def getNextSchemeElements(self):
        return self._next_elements

    """
    @desc Delete scheme_element with id as scheme_element_id
          from _next_elements dictionary (just remove elements connection,
          doesn`t delete element from scheme)
    @param scheme_element_id: string
    @return SchemeElement
    """
    def deleteNextSchemeElement(self, scheme_element_id):
        if self._next_elements.has_key(scheme_element_id):
            del self._next_elements[scheme_element_id]

    def getNextSchemeElementById(self, scheme_element_id):
        if self._next_elements.has_key(scheme_element_id):
            return self._next_elements[scheme_element_id]

    """
    @desc Add new element to _prev_elements
    @param scheme_element: SchemeElement
    @return SchemeElement
    """
    def addPreviousSchemeElement(self, scheme_element):
        self._prev_elements[scheme_element.getId()] = scheme_element
        return scheme_element

    """
    @desc Return dictionary of previous scheme elements
    @return dict of SchemeElement
    """
    def getPreviousSchemeElements(self):
        return self._prev_elements

    """
    @desc Delete scheme_element with id as scheme_element_id
          from _prev_elements dictionary (just remove elements connection,
          doesn`t delete element from scheme)
    @param scheme_element_id: string
    @return SchemeElement
    """

    def deletePreviousSchemeElementById(self, scheme_element_id):
        if self._prev_elements.has_key(scheme_element_id):
            del self._prev_elements[scheme_element_id]

    """
    @desc Load user, input and output parameters lists from element`s
          module. Return False if module isn`t defined.
    @return bool
    """

    def initParameters(self):
        if self._module != None:
            self._input_parameters = copy(self._module.getInputParameters())
            self._user_parameters = copy(self._module.getUserParameters())
            self._output_parameters = copy(self._module.getOutputParameters())
            return True
        return False

    """
    @desc Return user-defined-parameters list
    @return Parameters{}
    """
    def getUserParameters(self):
        return self._user_parameters

    """
    @desc Return input parameters list
    @return Parameters{}
    """
    def getInputParameters(self):
        return self._input_parameters

    """
    @desc Return output parameters list
    @return ParametersList
    """
    def getOutputParameters(self):
        return self._output_parameters

    """
    @desc Generate source code for element`s module realization
    @param language: int
    @return string
    """
    def generateCode(self, language):
        pass