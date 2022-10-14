# coding:utf-8
import os
import json
import error


class SearchByFileName(object):
    def __init__(self):
        self.files_result_dict = {}

    # 路径检查
    def __check_file_path(self, file_path):
        self.file_path = file_path
        # 类型检查
        if not isinstance(self.file_path, str):
            raise error.FromError("Check whether the file path is string")

        # 文件路径检查
        if not os.path.exists(self.file_path):
            raise error.NotPathError(f"not found {self.file_path}")

    # 名称检查
    def __check_file_name(self, file_name):
        self.file_name = file_name
        # 类型检查
        if not isinstance(self.file_name, str):
            raise error.FromError("Check whether the filename is string")

        # 长度检查
        if len(self.file_name) > 255 or self.file_name == "":
            raise error.SizeError("The filename cannot be empty or longer than 255 characters")

    def search_by_file_name(self, file_path, file_name) -> json:
        self.__check_file_path(file_path)
        # 获取文件名称列表
        search_path = os.path.abspath(file_path)
        file_list = os.listdir(search_path)

        # 筛选符合条件的名称
        count = 0
        while count < len(file_list):
            self.__check_file_name(file_name)
            if file_list[count].find(file_name) != -1:
                self.files_result_dict[count] = file_list[count]
            count += 1

        # 生成迭代器对象
        yield json.dumps(self.files_result_dict)


if __name__ == '__main__':
    test_cwd = os.getcwd()
    se = SearchByFileName()

    f_name = se.search_by_file_name(file_path=test_cwd, file_name="ea")
    for item in f_name:
        print(item)
