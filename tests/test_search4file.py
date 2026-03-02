import unittest

from search4file import __version__
from search4file.api.search_by_content import search_by_content, find_excel_data


class TestSearch(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'

    def test_search_by_content(self):
        search_by_content(search_path=r'./docs', search_content='程序员晚枫')

    def test_find_excel_data(self):
        find_excel_data(search_key='129-000064-10',
                        target_dir=r'C:\Users\Lenovo\Desktop\temp\test\excel')
