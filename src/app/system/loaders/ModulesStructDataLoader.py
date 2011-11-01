__author__="spas"
__date__ ="$31.10.2011 17:29:08$"

class ModulesStructDataLoader():
    def __init__(self, struct_file_url):
        self._struct_file_url = struct_file_url
        self._xml_etree = XMLDataLoader.loadDataFromFile(config.DATA_FOLDER + config.MODULES_STRUCT_FILE)
        self._root_element = self._xml_etree.get_root()

        self._groups = {}
        self._modules = {}

    def getGroupsList(self):
        for child in this._root_element:
            pass

    def getGroupModulesList(self, group_id):
        pass

    def initModule(self, module_id):
        pass