import glob

import os
from docx import Document
from pathlib import Path


class SearchByContent():
    def search_files(self, search_path, content):
        glob_path = glob.glob(search_path)
        for file_path in glob_path:  # for 循环判断递归查到的内容是文件夹还是文件
            if glob.os.path.isdir(file_path):  # 若是文件夹，继续将该文件夹的路径传给 search() 函数继续递归查找
                _path = glob.os.path.join(file_path, '*')
                self.search_files(_path, content)
            else:

                self.search_txt_file(file_path, content)
                self.search_word_file(file_path, content)

    def search_txt_file(self, search_path, content) -> None:
        """
        :param search_path:
        :param content:
        :return:
        """
        try:
            # 若是文件，则将该查询到的文件所在路径插入 final_result 空列表
            with open(search_path, 'r',
                      encoding='utf-8') as file:  # 利用 open() 函数读取文件，并通过 try...except... 捕获不可读的文件格式（.zip 格式）
                if content in file.read():
                    print('该文件内，包含：【{}】'.format(content) + ' | ' * 2 + search_path)
        except:
            pass

    def search_word_file(self, search_path, content):
        targetDocx = []
        if search_path.endswith("docx"):
            document = Document(search_path)
            all_paragraphs = document.paragraphs
            for paragraph in all_paragraphs:
                if paragraph.text.find(content) >= 0:
                    targetDocx.append(search_path)
        targetDocx = []
        if targetDocx:
            print(f'没有包含此内容的word文档')
        else:
            print(f'没有包含内容：{content}的word文档')
