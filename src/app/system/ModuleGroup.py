#
# Class for modules groups data loading and storing
#

__author__="spas"
__date__ ="$31.10.2011 18:24:10$"

class ModuleGroup(object):
    groups = {}
    
    def __init__(self):
        self._id = ''
        self._name = ''
        self._folder = ''
        self._icon = ''
        self._description = ''

        self._childGroups = {}
        self._childModules = {}

    def getChildrenDataFromLxml(self, lxml_node):
        for child_node in lxml_node:
            if child_node.tag == 'group':
                child_element = ModuleGroupData()
                child_element.getDataFromLxml(child_node)
                child_element.getChildrenDataFromLxml(child_node)

                self._childGroups[child_element.getId()] = child_element
            if child_node.tag == 'module':
                child_element = ModuleData()
                child_element.getDataFromLxml(child_node)

    def getDataFromLxml(self, lxml_node):
        self._id = lxml_node.get('id')
        self._name = lxml_node.get('name')
        self._folder = lxml_node.get('folder')
        self._icon = lxml_node.get('icon')
        self._description = lxml_node.text

        ModuleGroupData.groups[self._id] = self

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getFolder(self):
        return self._folder

    def getIcon(self):
        return self._icon

    def getDescription(self):
        return self._description

    def getChildGroups(self):
        return self._childGroups

    def getChildGroupById(self, group_id):
        if self._childGroups.has_key(group_id):
            return self._childGroups[group_id]

    def getChildModules(self):
        return self._childModules

    def getChildModuleById(self, module_id):
        if self._childModules.has_key(group_id):
            return self._childModules[group_id]