#
# Class for modules data loading and storing
#

__author__="spas"
__date__ ="$31.10.2011 18:24:01$"

class Module():
    modules = {}

    def __init__(self):
        self._base_data_loaded = false
        self._full_data_loaded = true

        self._id = ''
        self._name = ''
        self._folder = ''
        self._file = ''
        self._icon = ''
        self._description = ''

        self._inputParametersData = {}
        self._userParametersData = {}
        self._ouputParametersData = {}

        self._realizationsData = {}

    def getBaseDataFromLxml(self, lxml_node):
        self._id = lxml_node.get('id')
        self._name = lxml_node.get('name')
        self._folder = lxml_node.get('folder')
        self._file = lxml_node.get('file')
        self._icon = lxml_node.get('icon')
        self._description = lxml_node.text
        self._base_data_loaded = true

        ModuleData.modules[self._id] = self

    def getFullDataFromLxml(self, lxml_node):
        for child_node in lxml_node:
            if child_node.tag == 'input_parameters':
                for parameter_node in child_node:
                    parameterData = ParameterData()
                    parameterData.getDataFromLxml(parameter_node)
                    self._inputParametersData[parameterData.getId()] = parameterData
            if child_node.tag == 'output_parameters':
                for parameter_node in child_node:
                    parameterData = ParameterData()
                    parameterData.getDataFromLxml(parameter_node)
                    self._outputParametersData[parameterData.getId()] = parameterData
            if child_node.tag == 'user_parameters':
                for parameter_node in child_node:
                    parameterData = ParameterData()
                    parameterData.getDataFromLxml(parameter_node)
                    self._userParametersData[parameterData.getId()] = parameterData
            if child_node.tag == 'realizations':
                for realization_node in child_node:
                    realizationData = RealizationData()
                    realizationData.getDataFromLxml(realization_node)
                    self._realizationsData[realizationData.getId()] = realizationData

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
    return self._inputParametersData

def getInputParameterById(self, parameter_id):
    if self._inputParametersData.has_key(parameter_id):
        return self._inputParametersData[parameter_id]

def getUserParameters(self):
    return self._userParametersData

def getUserParameterById(self):
    if self._userParametersData.has_key(parameter_id):
        return self._userParametersData[parameter_id]

def getUserParameters(self):
    return self._outputParametersData

def getUserParameterById(self):
    if self._outputParametersData.has_key(parameter_id):
        return self._outputParametersData[parameter_id]