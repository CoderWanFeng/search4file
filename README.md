# search4file
pip install search4file
# 功能
- 通过内容查找文件
- 通过名称查找图片
- ocr识别图片内容
- 通过字幕、画面查找视频

# To List

有3类并行推进的任务：

## 1、查找逻辑

### 3个按照内容查找的接口，需要实现

[接口传送门](https://github.com/CoderWanFeng/search4file/blob/main/search4file/core/SearchByContent.py)
负责开发：[@yinzeyuan](https://github.com/yinzeyuan)

```python
    def search_pdf_file(self, file_path, search_content):
        pass

    def search_ppt_file(self, file_path, search_content):
        pass

    def search_excel_file(self, file_path, search_content):
        pass
```

### 1个按照文件名查找的接口，需要实现

[接口传送门](https://github.com/CoderWanFeng/search4file/blob/main/search4file/core/SearchByName.py)
负责开发：[@yinzeyuan](https://github.com/yinzeyuan)

```python
class SearchByName():

    # 搜索文件名的逻辑
    def search_files(self, search_path, search_content):
        pass
```
## 2、优化逻辑

优化内容，目前主要有：

1. 目前的word查找基于python-docx库，而这个库不支持mac、linux库。
    - 考虑改为解压docx的方式，对解压后的文件进行查找。
2. 目前对文件的查找，采用单线程同步遍历的方式，速度太慢。
    - 考虑改为进程 + 协程的异步方式，提高查询效率。
3. 增加OCR自动根据指定的图片内容，进行图片搜索。
    - 例如：用户输入：河流，查找出电脑里所有和河流有关的图片
4. 识别出视频里的内容。
    - 例如：用户输入：大山，查找出某个视频里，所有和大山有关的画面、字幕

## 3、发布该库的文章

