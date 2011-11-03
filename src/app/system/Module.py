#
# Class for modules data loading and storing
#

__author__="spas"
__date__ ="$31.10.2011 18:24:01$"

from app.system.config.xml import *

class Module():
    Modules = {}

    def __init__(self):
        self._base_data_loaded = False
        self._full_data_loaded = True

        self._id = ''
        self._name = ''
        self._folder = ''
        self._file = ''
        self._icon = ''
        self._description = ''

        self._input_parameters = {}
        self._user_parameters = {}
        self._ouput_parameters = {}

        self._realizations = {}

    def getBaseDataFromLxml(self, lxml_node):
        self._id = lxml_node.get(MODULE_ATTRIBUTE_ID)
        self._name = lxml_node.get(MODULE_ATTRIBUTE_NAME)
        self._folder = lxml_node.get(MODULE_ATTRIBUTE_FOLDER)
        self._file = lxml_node.get(MODULE_ATTRIBUTE_FILE)
        self._icon = lxml_node.get(MODULE_ATTRIBUTE_ICON)
        self._description = lxml_node.text
        self._base_data_loaded = True

        Module.Modules[self._id] = self

    def getFullDataFromLxml(self, lxml_node):
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
                    self._outputParametersData[parameter.getId()] = parameter
            if child_node.tag == USER_PARAMETERS_TAG:
                for parameter_node in child_node:
                    parameter = parameter()
                    parameter.getBaseDataFromLxml(parameter_node)
                    self._user_parameters[parameter.getId()] = parameter
            if child_node.tag == REALIZATIONS_TAG:
                for realization_node in child_node:
                    realization = realization()
                    realization.getBaseDataFromLxml(realization_node)
                    self._realizations[realization.getId()] = realization

    def getId(self):
        return self._id;

    def getName(self):
        return self._name;

    def getFolder(self):
        return self._folder;

    def getFile(self):
        return self._file;

    def getIcon(self):
        return self._icon;

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

    def getRealizations(self):
        return self._realizations

    def getRealizationById(self, realization_id):
        if self._realizations.has_key(realization_id):
            return self._realizations[realization_id]