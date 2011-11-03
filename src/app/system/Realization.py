# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="spas"
__date__ ="$01.11.2011 17:16:51$"

class Realization:
    def __init__(self):
        self._id = ''
        self._name = ''

        # folder with module realization files
        self._folder = ''
        self._main_file = ''

        # one of supported languages
        self._language = ''

        # source code or execution file?
        self._type = ''

        # base method name (or we should add here full method description,
        # for example UML-description)
        self._method = ''

        self._description = ''

        # Additional parameters, required for current realization of module
        self._input_parameters = {}
        self._user_parameters = {}
        self._output_parameters = {}

    def getBaseDataFromLxml(self, lxml_node):
        self._id = lxml_node.get(REALIZATION_ATTRIBUTE_ID)
        self._name = lxml_node.get(REALIZATION_ATTRIBUTE_NAME)
        self._folder = lxml_node.get(REALIZATION_ATTRIBUTE_FOLDER)
        self._main_file = lxml_node.get(REALIZATION_ATTRIBUTE_FILE)
        self._language = lxml_node.get(REALIZATION_ATTRIBUTE_LANGUAGE)
        self._type = lxml_node.get(REALIZATION_ATTRIBUTE_TYPE)
        self._method = lxml_node.get(REALIZATION_ATTRIBUTE_METHOD)

        for child_node in lxml_node:
            if child_node.tag == INPUT_PARAMETERS_TAG:
                for parameter_node in child_node:
                    parameter = parameter()
                    parameter.getBaseDataFromLxml(parameter_node)
                    self._input_parameters[parameter.getId()] = parameter
            if child_node.tag == OUTPUT_PARAMETERS_TAG:
                for parameter_node in child_node:
                    parameter = parameter()
                    parameter.getBaseDataFromLxml(parameter_node)
                    self._output_parameters[parameter.getId()] = parameter
            if child_node.tag == USER_PARAMETERS_TAG:
                for parameter_node in child_node:
                    parameter = parameter()
                    parameter.getBaseDataFromLxml(parameter_node)
                    self._user_parameters[parameter.getId()] = parameter
        self._description = lxml_node.text

    def getId(self):
        return self._id;

    def getName(self):
        return self._name

    def getFolder(self):
        return self._folder

    def getMainFile(self):
        return self._main_file

    def getLanguage(self):
        return self._language

    def getType(self):
        return self._type

    def getMethod(self):
        return self._method

    def getInputParameters(self):
        return self._input_parameters

    def getInputParameterById(self, parameter_id):
        if self._input_parameters.has_key(parameter_id):
            return self._input_parameters[parameter_id]

    def getUserParameters(self):
        return self._user_parameters

    def getUserParameterById(self):
        if self._user_parameters.has_key(parameter_id):
            return self._user_parameters[parameter_id]

    def getOutputParameters(self):
        return self._outputParametersData

    def getOutputParameterById(self):
        if self._outputParametersData.has_key(parameter_id):
            return self._outputParametersData[parameter_id]