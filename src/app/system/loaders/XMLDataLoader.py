from lxml import etree

__author__="spas"
__date__ ="$29.09.2011 11:18:09$"

"""
@desc Class for data loading from xml file
"""
class XMLDataLoader():
    """
    @param file_url: string
    @return lxml.etree
    """
    def loadDataFromFile(self, file_url):
        return etree.parse(file_url)
