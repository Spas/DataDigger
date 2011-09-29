__author__="spas"
__date__ ="$29.09.2011 11:16:11$"

class Module():

    def __init__(self):
        self._name = ''
        self._realizations = ModuleRealizationsList()
        self._userParametersList = ParametersList()
        self._inputParametersList = ParametersList()
        self._outputParametersList = ParametersList()

    def addUserParameter(self, parameter)
        """
        @desc Add new user-defined parameter
        @param parameter: app.system.Parameter
        @return app.system.Parameter
        """

    def getUserParametersList(self):
        """
        @desc Return user-defined-parameters list.
        @return app.system.ParametersList
        """

    def addInputParameter(self, parameter):
        """
        @desc Add new input parameter
        @param parameter: app.system.Parameter
        @return app.system.Parameter
        """

    def getInputParametersList(self):
        """
        @desc Return input parameters list
        @return app.system.ParametersList
        """

    def addOutputParameter(self, parameter):
        """
        @desc Add new output parameter
        @param parameter: app.system.Parameter
        @return app.system.Parameter
        """

    def getOutputParametersList(self):
        """
        @desc Return output parameters list
        @return app.system.ParametersList
        """

    def setName(self, name):
        """
        @desc Set module name if it isn`t defined
        @param name: string
        @return: string
        """

    def getName(self):
        """
        @desc Return module name
        @return string
        """

    def addRealization(self, realization):
        """
        @desc Add new module realization
        @param realization: app.system.code.realizations.ModuleRealization
        @return app.system.code.realizations.ModuleRealization
        """

    def getRealizationsList(self):
        """
        @desc Return module realizations list
        @return app.system.code.realizations.ModuleRealizationsList
        """