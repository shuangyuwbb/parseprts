#
# author wbb
# date 2020/11/20 16:23
# 解析xml文件，并且按一定格式写入文件

import os, json
import xml.etree.ElementTree as ET


class Parse:

    def __init__(self, path, new_path):
        self.path = path
        self.new_path = new_path
        self.obj = {}
        self.details = []

    def load_xml(self):
        L = []
        if os.path.exists(self.path):
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    if os.path.splitext(file)[1] == '.prts':
                        L.append(root + '\\' + file)
        return L

    def read_xml(self):
        data = []
        count = 0
        for index in range(len(self.load_xml())):
            count += 1
            root = ET.parse(self.load_xml()[index]).getroot()
            self.traverse_xml(root)

            data.append(self.details)
            self.details = []
        print('您一共读了{0}数据'.format(count))
        return data

    def traverse_xml(self, element):
        if len(element) > 0:
            for child in element:
                if child.tag == 'LwPolyline':
                    details_obj = {}
                    isFill = 'IsFill' in child.attrib
                    if isFill:
                        polyFlag = 'PolyFlag' in child.attrib
                        points = []
                        for point in child:
                            if 'X' not in point.attrib and 'Y' not in point.attrib:
                                points.append({'x': 0, 'y': 0})
                            elif 'X' not in point.attrib:
                                points.append({'x': 0, 'y': point.attrib['Y']})
                            elif 'Y' not in point.attrib:
                                points.append({'x': point.attrib['X'], 'y': 0})
                            else:
                                points.append({'x': point.attrib['X'], 'y': point.attrib['Y']})

                        details_obj['polyFlag'] = polyFlag
                        details_obj['point'] = points
                        self.details.append(details_obj)
                self.traverse_xml(child)
        else:
            print('解析到底！')
            return

    def write_json(self, ):
        with open(self.new_path, 'w') as file_object:
            file_object.write(json.dumps(self.read_xml()))
        pass


if __name__ == '__main__':
    path = input('请输入源文件绝对路径： ')
    new_path = path + '\data.json'
    parse = Parse(path, new_path)
    parse.write_json()
    print('输出的地址是：{0}\data.json'.format(path))
    print('按 --回车键-- 结束程序！')
    str = input()
