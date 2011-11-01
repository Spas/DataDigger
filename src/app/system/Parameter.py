#
# Class for parameters (input, output or user) data loading and storing
#

__author__="spas"
__date__ ="$01.11.2011 17:08:29$"

class Parameter:
    def __init__(self):
        self._id = ''
        self._name = ''
        self._type = ''
        self._default = ''
        self._description = ''

    def getDataFromLxml(self, lxml_node):
        self._id = lxml_node.get('id')
        self._name = lxml_node.get('name')
        self._type = lxml_node.get('type')
        self._default = lxml_node.get('default')
        self._description = lxml_node.text

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getDefault(self):
        return self._default

    def getDescription(self):
        return self._description