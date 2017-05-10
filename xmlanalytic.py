#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
import tools.xmlUtil as xmlUtil

class xmlanalytic:

    def __init__(self,filename):
        self.sysXMLDict = {}
        try:
            self.three = ET.parse(filename)
        except Exception as e:
            print("Error:cannot parse file:" + filename + ".\n" + e.__str__())
            sys.exit(1)


    def findmondel(self,path):
        return self.three.findall(path)

    def getXMLDict(self,root):
        for child in root:
            self.sysXMLDict[child.tag] = child.attrib
            self.sysXMLDict[child.tag] = child.text
        return self.sysXMLDict

if (__name__ == '__main__'):
    xa = xmlanalytic("test.xml")
    path = xa.findmondel("property")
    xa.getXMLDict(path)
    print(xa.sysXMLDict)
    xu = xmlUtil()
