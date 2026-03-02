# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@读者群     ：https://www.python4office.cn/wechat-group/
@个人网站 ：www.python-office.com
@Date    ：2023/4/5 11:02 
@Description     ：
'''
from win32com.client import Dispatch

word = Dispatch('Word.Application')  # 打开word应用程序
# word = DispatchEx('Word.Application') # 启动独立的进程
word.Visible = 0  # 后台运行,不显示
word.DisplayAlerts = 0  # 不警告
path = r'D:\test\py310\word_dev\word\doc\（复杂）韦鸿钰非法侵入计算机信息系统一审刑事判决书.doc'
doc = word.Documents.Open(FileName=path, Encoding='gbk')
print(doc)
# for para in doc.paragraphs:
#     print(para)
