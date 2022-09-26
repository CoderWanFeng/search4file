import glob
import json
import os
import pandas as pd
from docx import Document
from search4file.core import SpecialExcel


class SearchByContent():
    # 初始化输出结果
    def __init__(self):
        self.search_result_dict = {
            'search_path': None,
            'search_content': None,
            # 初始化、找不到时：
            'search_result': {}
        }
        self.files_result_dict = {}
        self.word_result_dict = {}
        self.excel_result_dict = {}
        self.ppt_result_dict = {}
        self.pdf_result_dict = {}

    # 格式化返回内容
    def create_return_result(self, search_path, search_content):
        search_path = os.path.abspath(search_path)
        # 查询路径在哪里
        self.search_result_dict['search_path'] = search_path
        # 查询内容是什么
        self.search_result_dict['search_content'] = search_content
        # 返回纯文本
        if len(self.files_result_dict) > 0:
            self.search_result_dict['search_result']['files'] = self.files_result_dict
        # 返回word
        if len(self.word_result_dict) > 0:
            self.search_result_dict['search_result']['word'] = self.word_result_dict
        # 返回excel
        if len(self.excel_result_dict) > 0:
            self.search_result_dict['search_result']['excel'] = self.excel_result_dict
        # 转换为json格式返回
        return json.dumps(self.search_result_dict, indent=4, ensure_ascii=False)

    # 搜索内容的逻辑
    def search_files(self, search_path, search_content):
        glob_path = glob.glob(search_path)  # 获取全部路径
        for file_path in glob_path:  # for 循环判断递归查到的内容是文件夹还是文件
            if glob.os.path.isdir(file_path):  # 若是文件夹，继续将该文件夹的路径传给 search() 函数继续递归查找
                _path = glob.os.path.join(file_path, '*')
                self.search_files(_path, search_content)
            else:
                if file_path.endswith("docx"):
                    self.search_word_file(file_path, search_content)
                elif file_path.endswith("xlsx") or file_path.endswith("xls"):
                    self.search_excel_file(file_path, search_content)
                else:
                    self.search_txt_file(file_path, search_content)

        return self.create_return_result(search_path, search_content)

    ####################################
    # 搜索 纯文本 文件
    ####################################
    def search_txt_file(self, file_path, search_content) -> None:
        """
        :param search_path:
        :param content:
        :return: dict
        """
        # 若是文件，则将该查询到的文件所在路径插入 final_result 空列表
        with open(file_path, 'r',
                  encoding='utf-8') as file:  # 利用 open() 函数读取文件，并通过 try...except... 捕获不可读的文件格式（.zip 格式）
            if search_content in file.read():
                self.files_result_dict[str(len(self.files_result_dict) + 1)] = file_path

    ####################################
    # 搜索 word 文件
    ####################################
    def search_word_file(self, file_path, search_content):

        document = Document(file_path)
        all_paragraphs = document.paragraphs
        for paragraph in all_paragraphs:
            if paragraph.text.find(search_content) >= 0:
                self.word_result_dict[str(len(self.word_result_dict) + 1)] = file_path

    ####################################
    # 搜索 pdf 文件
    ####################################
    def search_pdf_file(self, file_path, search_content):
        pass

    ####################################
    # 搜索 ppt 文件
    ####################################
    def search_ppt_file(self, file_path, search_content):
        pass

    ####################################
    # 搜索 excel 文件
    ####################################
    def search_excel_file(self, file_path, search_content):
        df = pd.read_excel(file_path, sheet_name=None, header=None)
        for sheet in df.values():
            for row in sheet.itertuples():
                if search_content in row:
                    self.excel_result_dict[str(len(self.excel_result_dict) + 1)] = file_path
