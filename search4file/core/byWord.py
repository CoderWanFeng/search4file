import os
from docx import Document
from pathlib import Path

searchTarget = input("请输入查找内容：")
searchPath = input("请输入查找路径：")
path = Path(searchPath)
targetDocx = []
# 存储包含查找内容的文件名
file_path_dict = {}
for root, dirs, files in os.walk(searchPath):
    for file in files:
        if file.endswith("docx"):
            file_path_dict[file] = (path / file)
# 从Excel抄来的，合并路径用
for filename, filepath in file_path_dict.items():
    document = Document(filepath)
    all_paragraphs = document.paragraphs
    for paragraph in all_paragraphs:
        if paragraph.text.find(searchTarget) >= 0:
            targetDocx.append(filename)
print(targetDocx)
