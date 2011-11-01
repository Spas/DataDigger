"""
Класс-фабрика для получения объектов модулей и их реализаций
"""

__author__="spas"
__date__ ="$29.09.2011 11:16:30$"

class ModulesFactory():
    """
    Dictionary with base modules data.
    """
    modules_data_loaded = false
    modules_groups = {}
    modules_data = {}

    def loadModulesStructData(self):
        ModulesFactory.modules_data_loaded = false

        data_loader = XMLDataLoader()
        modules_data_etree = data_loader

        ModulesFactory.modules_data_loaded = true

    """
    @param module_id string
    @return app.system.Module
    """
    @classmethod
    def getModuleById(cls, module_id):
        pass

    """
    @return app.system.Module[]
    """
    @classmethod
    def getModulesList(cls):
        pass