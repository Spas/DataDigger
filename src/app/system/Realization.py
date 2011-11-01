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

    def getDataFromLxml(self, lxml_node):
        self._id = lxml_node.get('id')
        self._name = lxml_node.get('name')
        self._folder = lxml_node.get('folder')
        self._main_file = lxml_node.get('main_file')
        self._language = lxml_node.get('language')
        self._type = lxml_node.get('type')
        self._method = lxml_node.get('method')
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