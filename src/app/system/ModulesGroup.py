#
# Class for modules groups data loading and storing
#

__author__="spas"
__date__ ="$31.10.2011 18:24:10$"

from app.system.Module import Module
from app.system.config.xml import *

class ModulesGroup(object):
    Groups = {}
    
    def __init__(self):
        self._id = ''
        self._name = ''
        self._folder = ''
        self._icon = ''
        self._description = ''

        self._child_groups = {}
        self._child_modules = {}

    def getChildrenDataFromLxml(self, lxml_node):
        for child_node in lxml_node:
            if child_node.tag == MODULES_GROUP_TAG:
                child_element = ModulesGroup()
                child_element.getBaseDataFromLxml(child_node)
                child_element.getChildrenDataFromLxml(child_node)

                self._child_groups[child_element.getId()] = child_element
            if child_node.tag == MODULE_TAG:
                child_element = Module()
                child_element.getBaseDataFromLxml(child_node)

    def getBaseDataFromLxml(self, lxml_node):
        self._id = lxml_node.get(MODULES_GROUP_ATTRIBUTE_ID)
        self._name = lxml_node.get(MODULES_GROUP_ATTRIBUTE_NAME)
        self._folder = lxml_node.get(MODULES_GROUP_ATTRIBUTE_FOLDER)
        self._icon = lxml_node.get(MODULES_GROUP_ATTRIBUTE_ICON)
        self._description = lxml_node.text

        ModulesGroup.Groups[self._id] = self

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
        return self._child_groups

    def getChildGroupById(self, group_id):
        if self._child_groups.has_key(group_id):
            return self._child_groups[group_id]

    def getChildModules(self):
        return self._child_modules

    def getChildModuleById(self, group_id):
        if self._child_modules.has_key(group_id):
            return self._child_modules[group_id]