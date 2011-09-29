__author__="spas"
__date__ ="$29.09.2011 11:22:47$"

from abc import ABCMeta, abstractmethod, abstractproperty

class CodeProcessor():
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute():
        """ Функция выполнения программного кода """