__author__="spas"
__date__ ="$29.09.2011 11:17:48$"

class ParametersList():
    def __init__(self):
        self._parameters = {}

    def addParameter(self, parameter):
        """
        @desc Add new parameter
        @param parameter: app.system.Parameter
        @return app.system.Parameter
        """

    def getParameterByName(self, parameter_name):
        """
        @desc Return parameter with same name as parameter_name
        @param parameter_name: string
        @return app.system.Parameter
        """

    def getParametersNames(self):
        """
        @desc Return array with all parameters names
        @return string[]
        """