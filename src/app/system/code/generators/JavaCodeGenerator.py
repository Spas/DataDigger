"""
Класс для преобразования схемы выполнения функций на языке Java в единую программу
"""

__author__="spas"
__date__ ="$29.09.2011 11:22:08$"

class JavaCodeGenerator(CodeGenerator):

    def __init__(self):
        self._name = 'JavaCodeGenerator'

    def generateCode(self):
        """ Генерация кода на языке Java """
