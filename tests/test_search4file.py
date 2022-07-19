import unittest

from search4file import __version__
from search4file.api.search4file import search_by_content


class TestSearch(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'

    def test_search(self):
        search_by_content(search_path=r'./docs',content='test')


