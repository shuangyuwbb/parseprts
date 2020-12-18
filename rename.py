#
# author wbb
# date 2020/11/20 16:23
# 修改文件名后缀



import os

class Ren:
    def __init__(self, file_dir, new_str):
        self.file_dir = file_dir
        self.new_str = new_str
        print('33')

    def file_name(self):
        L = []
        if os.path.exists(self.file_dir):
            for root, dirs, files in os.walk(self.file_dir):
                # print(files)
                for file in files:
                    if os.path.splitext(file)[1] == '.prts':
                        # print(os.path.splitext(file)[0])
                        L.append(os.path.join(root, file))
        else:
            print('文件夹不存在！')

        return L
    def ren_name(self):

        for file in self.file_name():
            print(file)
            try:
                fileInfo = os.path.splitext(file)
                newName = fileInfo[0] + '.xml'
                os.rename(file, newName)
            except(FileExistsError):
                print('文件已存在')

fiel_dir = 'D:\code\Python\parsePrts\data'
new_str = ''

rename = Ren(fiel_dir, new_str)
rename.ren_name()

