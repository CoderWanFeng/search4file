import glob


class SearchByContent():
    def search_txt_file(self, search_path, content) -> None:
        """
        :param path:
        :param content:
        :return:
        """
        glob_path = glob.glob(search_path)
        for file_path in glob_path:  # for 循环判断递归查到的内容是文件夹还是文件
            if glob.os.path.isdir(file_path):  # 若是文件夹，继续将该文件夹的路径传给 search() 函数继续递归查找
                _path = glob.os.path.join(file_path, '*')
                self.search_by_content(_path, content)
            else:  # 若是文件，则将该查询到的文件所在路径插入 final_result 空列表
                try:
                    with open(file_path, 'r') as file:  # 利用 open() 函数读取文件，并通过 try...except... 捕获不可读的文件格式（.zip 格式）
                        if content in file.read():
                            print('该文件内，包含：【{}】'.format(content) + ' | ' * 2 + file_path)
                except:
                    continue

    def search_word_file(self, search_path, content):
        pass
