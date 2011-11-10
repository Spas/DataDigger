# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="spas"
__date__ ="$29.09.2011 11:12:23$"

from app.system.ModulesFactory import ModulesFactory
from app.system.config.languages import *
from app.system.SchemeElement import SchemeElement

if __name__ == "__main__":
    ModulesFactory.loadModulesStructData()

    print(ModulesFactory.getModulesIds())

    relief_module = ModulesFactory.getModuleById('relief')
    relief_realization = relief_module.getRealizationByLanguage(LANGUAGE_C)

    csv_loading_module = ModulesFactory.getModuleById('csv_file_read')
    csv_loading_realization = csv_loading_module.getRealizationByLanguage(LANGUAGE_C)

    first_element = SchemeElement()
