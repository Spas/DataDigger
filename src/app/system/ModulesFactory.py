#
# Factory for Modules and ModulesGroups
#

__author__="spas"
__date__ ="$29.09.2011 11:16:30$"

from app.system.loaders.XMLDataLoader import XMLDataLoader
from app.system.config.links import *
from app.system.config.xml import *
from app.system.ModulesGroup import ModulesGroup
from app.system.Module import Module

class ModulesFactory():
    modules_data_loaded = False

    Base_groups = {}

    @staticmethod
    def loadModulesStructData():
        ModulesFactory.modules_data_loaded = False

        data_loader = XMLDataLoader()
        modules_data_etree = data_loader.loadDataFromFile(DATA_FOLDER + MODULES_STRUCT_FILE)
        root_node = modules_data_etree.getroot()
        for node in root_node:
            if node.tag == MODULES_GROUP_TAG:
                modules_group = ModulesGroup()
                modules_group.getBaseDataFromLxml(node)
                modules_group.getChildrenDataFromLxml(node)

                ModulesFactory.Base_groups[modules_group.getId()] = modules_group

        ModulesFactory.modules_data_loaded = True

    """
    @param module_id string
    @return app.system.Module
    """
    @staticmethod
    def getModuleById(module_id):
        if Module.Modules.has_key(module_id):
            return Module.Modules[module_id]

    @staticmethod
    def getBaseGroups():
        return ModulesFactory.Base_groups
    
    """
    @return app.system.Module[]
    """
    @staticmethod
    def getModulesGroupById(group_id):
        if ModulesGroup.Groups.has_key(group_id):
            return ModulesGroup.Groups[group_id]