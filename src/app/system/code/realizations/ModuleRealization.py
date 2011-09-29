"""
Базовый абстрактный класс для генерации кода функции вызова модуля.
"""

__author__="spas"
__date__ ="$29.09.2011 11:18:58$"

from abc import ABCMeta, abstractmethod, abstractproperty

class ModuleRealization():
    __metaclass__ = ABCMeta

    def generateDefaultCode(self):
        self.generatePythonCode()

    @abstractmethod
    def generatePythonCode():
        pass

    @abstractmethod
    def generateRCode():
        pass

    @abstractmethod
    def generateJavaCode():
        pass