#!/usr/bin/python
# -*- coding=utf-8 -*-
# version: 0.1

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import sys

class xmlUtil():
    """
        对xml配置文件进行实时修改， 
        1.增加、删除 某些节点
        2.增加，删除，修改某个节点下的某些属性
        3.增加，删除，修改某些节点的文本
    """
    def __init__(self,filename):
        """
        初始化方法
        :param filename: 文件名称
        """
        self.sysXMLDict = {}
        try:
            self.three = ET.parse(filename)
        except Exception as e:
            print("Error:cannot parse file:" + filename + ".\n" + e.__str__())
            sys.exit(1)

    @staticmethod
    def write_xml(tree, out_path):
        '''''将xml文件写出 
           :param tree: xml树 
           :param out_path: 写出路径'''
        tree.write(out_path, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def if_match(node, kv_map):
        '''''判断某个节点是否包含所有传入参数属性 
           :param node: 节点 
           :param kv_map: 属性及属性值组成的map'''
        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True


    # ---------------search -----
    @staticmethod
    def find_nodes(tree, path):
        '''''查找某个路径匹配的所有节点 
           :param tree: xml树 
           :param path: 节点路径'''
        return tree.findall(path)


    def get_node_by_keyvalue(self,nodelist, kv_map):
        '''''根据属性及属性值定位符合的节点，返回节点 
           :param nodelist: 节点列表 
           :param kv_map: 匹配属性及属性值map'''
        result_nodes = []
        for node in nodelist:
            if self.if_match(node, kv_map):
                result_nodes.append(node)
        return result_nodes


    # ---------------change -----
    @staticmethod
    def change_node_properties(nodelist, kv_map, is_delete=False):
        '''''修改/增加 /删除 节点的属性及属性值 
           :param nodelist: 节点列表 
           :param kv_map:属性及属性值map
           :param is_delete 是否删除，默认False'''
        for node in nodelist:
            for key in kv_map:
                if is_delete:
                    if key in node.attrib:
                        del node.attrib[key]
                else:
                    node.set(key, kv_map.get(key))

    @staticmethod
    def change_node_text(nodelist, text, is_add=False, is_delete=False):
        '''''改变/增加/删除一个节点的文本 
           :param nodelist:节点列表 
           :param text : 更新后的文本
           :param is_add 是否增加，默认False
           :param is_delete 是否删除，默认False '''
        for node in nodelist:
            if is_add:
                node.text += text
            elif is_delete:
                node.text = ""
            else:
                node.text = text

    @staticmethod
    def create_node(tag, property_map, content):
        '''''新造一个节点 
           :param tag:节点标签 
           :param property_map:属性及属性值map 
           :param content: 节点闭合标签里的文本内容 
           :return: 新节点'''
        element = Element(tag, property_map)
        element.text = content
        return element

    @staticmethod
    def add_child_node(nodelist, element):
        '''''给一个节点添加子节点 
           :param nodelist: 节点列表 
           :param element: 子节点'''
        for node in nodelist:
            node.append(element)


    def del_node_by_tagkeyvalue(self,nodelist, tag, kv_map):
        '''''同属性及属性值定位一个节点，并删除之 
           :param nodelist: 父节点列表 
           :param tag:子节点标签 
           :param kv_map: 属性及属性值列表'''
        for parent_node in nodelist:
            children = parent_node.getchildren()
            for child in children:
                if child.tag == tag and self.if_match(child, kv_map):
                    parent_node.remove(child)


    def getXMLDict(self,root):
        """
        按照节点输出json字符串
        :param root:要输出的根节点 
        :return: json字符串
        """
        for child in root:
            self.sysXMLDict[child.tag] = child.attrib
            self.sysXMLDict[child.tag] = child.text
        return self.sysXMLDict

if __name__ == "__main__":

    # 实例化对象
    xu = xmlUtil("test.xml")

    # 1. 读取xml文件树
    tree = xu.three

    # 2. 属性修改
    # A. 找到父节点
    nodes = xu.find_nodes(tree, "processers/processer")
    # print(nodes)
    # B. 通过属性准确定位子节点
    result_nodes = xu.get_node_by_keyvalue(nodes, {"name": "BProcesser"})
    # C. 修改节点属性
    xu.change_node_properties(result_nodes, {"age": "1"})
    # D. 删除节点属性
    xu.change_node_properties(result_nodes, {"value": ""}, True)

    # 3. 节点修改
    # A.新建节点
    a = xu.create_node("person", {"age": "15", "money": "200000"}, "this is the firest content")
    # B.插入到父节点之下
    xu.add_child_node(result_nodes, a)

    # 4. 删除节点
    # 定位父节点
    del_parent_nodes = xu.find_nodes(tree, "processers/services/service")
    # 准确定位子节点并删除之
    target_del_node = xu.del_node_by_tagkeyvalue(del_parent_nodes, "chain", {"sequency": "chain1"})

    # 5. 修改节点文本
    # 定位节点
    text_nodes = xu.get_node_by_keyvalue(xu.find_nodes(tree, "processers/services/service/chain"), {"sequency": "chain3"})
    xu.change_node_text(text_nodes, "new text")

    # 6. 输出到结果文件
    xu.write_xml(tree, "./out.xml")

    #  7 输出节点
    print(xu.getXMLDict(nodes))

