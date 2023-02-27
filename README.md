

<p align="center" id='支付宝'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/UsFs6ooDspyhhKMleKTVpw'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2Falipay.jpg" width="100%"/>
    </a>   
</p>


<p align="center" id='外卖'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/KfjQBf1n_slziZxeOQnhzQ'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F%E8%81%94%E7%9B%9F%E5%B9%BF%E5%91%8A%2F%E5%A4%96%E5%8D%96-1040-100.jpg" width="100%"/>
    </a>   
</p>





<p align="center" name="图标-github">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng/python-office'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
  	<a href="https://mp.weixin.qq.com/s/Jf_EVdKlVnHhK68fW5OA6A">
	<img src="https://img.shields.io/badge/QQ-1090738447-orange"/>
  </a>
    	<a href="https://mp.weixin.qq.com/s/wx-JkgOUoJhb-7ZESxl93w">
	<img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1-%E4%BA%A4%E6%B5%81%E7%BE%A4-brightgreen"/>
  </a>
</p>


# search4file
pip install search4file

你好，我是Python程序员晚枫。这个库实现的功能：根据文件内容，搜索文件位置。
> 已经集成到python-office里了👉[视频教程](https://www.bilibili.com/video/BV13P411n77G)
开发者微信：[CoderWanFeng](https://mp.weixin.qq.com/s/j-t09tlOLZhC4Rhc77SmYw)
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

## 3、交流群
![CoderWanFeng](https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/python-office-qr.jpg)

<p align="center" id='腾讯云-banner'>
    <a target="_blank" href='https://url.cn/Z4lzPLaF'>
    <img src="https://website-python-1300615378.cos.ap-nanjing.myqcloud.com/ads%2F1040x100-tencent.jpg" width="100%"/>
    </a>   
</p>
